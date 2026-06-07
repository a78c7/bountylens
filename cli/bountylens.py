#!/usr/bin/env python3
"""BountyLens CLI.

Analyze public GitHub issue text for bounty signals, false-positive signals,
and task risk flags. The tool uses Python standard library only and does not
read cookies, tokens, or local account state.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.request
from dataclasses import dataclass, asdict
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable, List, Optional


VERSION = "0.1.0"

BOUNTY_KEYWORDS = [
    "bounty",
    "reward",
    "funded",
    "issuehunt",
    "opire",
    "algora",
    "bountysource",
    "gitcoin",
    "sponsor",
    "backer",
    "pull request to get",
    "submit a pull request",
]

PLATFORM_KEYWORDS = [
    ("IssueHunt", ["issuehunt", "issue hunt"]),
    ("Opire", ["opire"]),
    ("Algora", ["algora"]),
    ("Bountysource", ["bountysource", "bounty source"]),
    ("Gitcoin", ["gitcoin"]),
]

FAKE_OR_WEAK_SIGNALS = [
    "no reward yet",
    "reward failed",
    "failed to create reward",
    "below minimum reward",
    "test bounty",
    "demo bounty",
    "placeholder",
    "hackathon winner",
    "bug bounty program",
    "vulnerability disclosure",
]

DIRECT_PR_SIGNALS = [
    "competing pr",
    "already has a pr",
    "already has pr",
    "already opened a pull request",
    "open pull request",
    "open pr",
    "linked pr",
    "duplicate pr",
    "someone is working on",
    "there is a pr",
    "there is already a pull request",
]

FORBIDDEN_GROUPS = {
    "security_vulnerability": [
        "security",
        "vulnerability",
        "exploit",
        "rce",
        "xss",
        "csrf",
        "ssrf",
    ],
    "auth_token_secret": [
        "auth",
        "oauth",
        "password",
        "token",
        "secret",
        "credential",
    ],
    "payment_wallet_crypto_kyc": [
        "payment",
        "billing",
        "stripe",
        "wallet",
        "crypto",
        "kyc",
    ],
    "database_migration": [
        "database migration",
        "production database",
        "destructive migration",
    ],
}

EXTERNAL_ENVIRONMENT_GROUPS = {
    "real_device_or_hardware": ["real device", "hardware"],
    "remote_or_ui_environment": ["vnc", "minecraft server", "blender ui"],
    "deployment_or_cloud_account": [
        "google apps script deployment",
        "github pages settings",
        "cloud account",
        "api key",
        "admin account",
        "paid saas",
        "production credentials",
    ],
}

AMOUNT_PATTERN = re.compile(
    r"(?i)(?:\$[0-9][0-9,]*(?:\.[0-9]{1,2})?"
    r"|\b(?:USD|USDC|DAI|ICP)\s*[0-9][0-9,]*(?:\.[0-9]{1,2})?"
    r"|\b[0-9][0-9,]*(?:\.[0-9]{1,2})?\s*(?:USD|USDC|DAI|ICP)\b)"
)

TITLE_PATTERN = re.compile(r"(?is)<title[^>]*>(.*?)</title>")


@dataclass
class AnalysisResult:
    url: Optional[str]
    title: Optional[str]
    bounty_signal: bool
    platform_signal: str
    possible_amounts: List[str]
    risk_flags: List[str]
    forbidden_flags: List[str]
    external_environment_flags: List[str]
    confidence: str
    recommendation: str
    suggested_next_step: str


class IssueHTMLTextExtractor(HTMLParser):
    """Small HTML text extractor for public issue pages and local examples."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._skip_depth = 0
        self.parts: List[str] = []
        self.title_parts: List[str] = []
        self._in_title = False

    def handle_starttag(self, tag: str, attrs) -> None:  # type: ignore[no-untyped-def]
        tag = tag.lower()
        if tag in {"script", "style", "noscript", "svg"}:
            self._skip_depth += 1
        if tag == "title":
            self._in_title = True

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "noscript", "svg"} and self._skip_depth:
            self._skip_depth -= 1
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        cleaned = " ".join(data.split())
        if not cleaned:
            return
        if self._in_title:
            self.title_parts.append(cleaned)
        if self._skip_depth == 0:
            self.parts.append(cleaned)

    @property
    def text(self) -> str:
        return "\n".join(self.parts)

    @property
    def title(self) -> Optional[str]:
        title = " ".join(self.title_parts).strip()
        return title or None


def normalize(text: str) -> str:
    return " ".join(html.unescape(text).lower().split())


def unique_preserve_order(items: Iterable[str]) -> List[str]:
    seen = set()
    output = []
    for item in items:
        key = item.lower()
        if key not in seen:
            seen.add(key)
            output.append(item)
    return output


def extract_amounts(text: str) -> List[str]:
    return unique_preserve_order(match.group(0).strip() for match in AMOUNT_PATTERN.finditer(text))


def detect_platform(normalized_text: str) -> str:
    for platform, keywords in PLATFORM_KEYWORDS:
        if any(keyword in normalized_text for keyword in keywords):
            return platform
    return "Unknown"


def detect_group_flags(normalized_text: str, groups: dict[str, list[str]]) -> List[str]:
    flags = []
    for group, keywords in groups.items():
        if any(keyword in normalized_text for keyword in keywords):
            flags.append(group)
    return flags


def detect_risk_flags(normalized_text: str) -> List[str]:
    flags = []
    if any(keyword in normalized_text for keyword in DIRECT_PR_SIGNALS):
        flags.append("direct_competing_pr_likely")
    if any(keyword in normalized_text for keyword in FAKE_OR_WEAK_SIGNALS):
        flags.append("fake_or_weak_bounty_signal")
    return flags


def extract_title_from_html(raw_html: str) -> Optional[str]:
    match = TITLE_PATTERN.search(raw_html)
    if not match:
        return None
    title = html.unescape(re.sub(r"\s+", " ", match.group(1))).strip()
    return title or None


def html_to_text(raw_html: str) -> tuple[str, Optional[str]]:
    parser = IssueHTMLTextExtractor()
    parser.feed(raw_html)
    return parser.text, parser.title or extract_title_from_html(raw_html)


def analyze_issue_text(text: str, *, url: Optional[str] = None, title: Optional[str] = None) -> AnalysisResult:
    normalized_text = normalize(text)
    possible_amounts = extract_amounts(text)
    platform_signal = detect_platform(normalized_text)
    bounty_keyword_signal = any(keyword in normalized_text for keyword in BOUNTY_KEYWORDS)
    bounty_signal = bounty_keyword_signal or platform_signal != "Unknown"
    risk_flags = detect_risk_flags(normalized_text)
    forbidden_flags = detect_group_flags(normalized_text, FORBIDDEN_GROUPS)
    external_environment_flags = detect_group_flags(normalized_text, EXTERNAL_ENVIRONMENT_GROUPS)

    if not bounty_signal:
        recommendation = "not_a_bounty"
        confidence = "high"
        suggested_next_step = "Skip bounty workflow. Treat this as a normal open source issue."
    elif forbidden_flags:
        recommendation = "avoid"
        confidence = "high"
        suggested_next_step = "Avoid this candidate or get explicit expert review before any work."
    elif "fake_or_weak_bounty_signal" in risk_flags:
        recommendation = "avoid"
        confidence = "medium"
        suggested_next_step = "Do not assume payment exists. Confirm platform status manually before spending time."
    elif external_environment_flags or "direct_competing_pr_likely" in risk_flags or not possible_amounts:
        recommendation = "manual_confirmation_needed"
        confidence = "medium"
        suggested_next_step = "Open the issue and bounty platform manually. Confirm payout, ownership, existing PRs, and testability."
    else:
        recommendation = "good_candidate_to_review"
        confidence = "high" if platform_signal != "Unknown" else "medium"
        suggested_next_step = "Run a read-only Codex candidate review before attempting implementation."

    return AnalysisResult(
        url=url,
        title=title,
        bounty_signal=bounty_signal,
        platform_signal=platform_signal,
        possible_amounts=possible_amounts,
        risk_flags=risk_flags,
        forbidden_flags=forbidden_flags,
        external_environment_flags=external_environment_flags,
        confidence=confidence,
        recommendation=recommendation,
        suggested_next_step=suggested_next_step,
    )


def fetch_url(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": f"BountyLens/{VERSION} public-issue-analyzer",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:  # nosec: public URL CLI fetch
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def result_to_markdown(result: AnalysisResult) -> str:
    def bullet_list(items: List[str]) -> str:
        if not items:
            return "- none"
        return "\n".join(f"- {item}" for item in items)

    lines = [
        "# BountyLens Report",
        "",
        f"- url: {result.url or 'n/a'}",
        f"- title: {result.title or 'n/a'}",
        f"- bounty_signal: {str(result.bounty_signal).lower()}",
        f"- platform_signal: {result.platform_signal}",
        f"- confidence: {result.confidence}",
        f"- recommendation: {result.recommendation}",
        "",
        "## Possible Amounts",
        "",
        bullet_list(result.possible_amounts),
        "",
        "## Risk Flags",
        "",
        bullet_list(result.risk_flags),
        "",
        "## Forbidden Flags",
        "",
        bullet_list(result.forbidden_flags),
        "",
        "## External Environment Flags",
        "",
        bullet_list(result.external_environment_flags),
        "",
        "## Suggested Next Step",
        "",
        result.suggested_next_step,
        "",
    ]
    return "\n".join(lines)


def result_to_json(result: AnalysisResult) -> str:
    return json.dumps(asdict(result), indent=2, sort_keys=True)


def read_input(args: argparse.Namespace) -> tuple[str, Optional[str], Optional[str]]:
    provided = [bool(args.url), bool(args.html), bool(args.text)]
    if sum(provided) != 1:
        raise ValueError("Provide exactly one input: --url, --html, or --text.")

    if args.url:
        raw_html = fetch_url(args.url)
        text, title = html_to_text(raw_html)
        return text, args.url, title

    if args.html:
        raw_html = Path(args.html).read_text(encoding="utf-8")
        text, title = html_to_text(raw_html)
        return text, None, title

    return args.text, None, None


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Analyze a GitHub issue for bounty signals and risk flags.")
    parser.add_argument("--url", help="Public GitHub issue URL to fetch and analyze.")
    parser.add_argument("--html", help="Local HTML file to analyze.")
    parser.add_argument("--text", help="Raw issue text to analyze.")
    parser.add_argument("--output", help="Write the report to this path instead of stdout.")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of Markdown.")
    parser.add_argument("--version", action="version", version=f"BountyLens {VERSION}")
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    try:
        text, url, title = read_input(args)
        result = analyze_issue_text(text, url=url, title=title)
        output = result_to_json(result) if args.json else result_to_markdown(result)
        if args.output:
            Path(args.output).write_text(output, encoding="utf-8")
        else:
            print(output)
        return 0
    except Exception as exc:  # pragma: no cover - exercised through CLI behavior
        print(f"bountylens: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
