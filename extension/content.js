(function () {
  "use strict";

  const VERSION = "0.1.0";

  const bountyKeywords = [
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
  ];

  const platformKeywords = [
    ["IssueHunt", ["issuehunt", "issue hunt"]],
    ["Opire", ["opire"]],
    ["Algora", ["algora"]],
    ["Bountysource", ["bountysource", "bounty source"]],
    ["Gitcoin", ["gitcoin"]],
  ];

  const fakeSignals = [
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
  ];

  const directPrSignals = [
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
  ];

  const riskGroups = {
    "security / vulnerability": ["security", "vulnerability", "exploit", "rce", "xss", "csrf", "ssrf"],
    "auth / token / secret": ["auth", "oauth", "password", "token", "secret", "credential"],
    "payment / wallet / crypto / KYC": ["payment", "billing", "stripe", "wallet", "crypto", "kyc"],
    "database migration": ["database migration", "production database", "destructive migration"],
    "external environment required": [
      "real device",
      "hardware",
      "vnc",
      "minecraft server",
      "blender ui",
      "google apps script deployment",
      "github pages settings",
      "cloud account",
      "api key",
      "admin account",
      "paid saas",
      "production credentials",
    ],
  };

  const amountPattern =
    /(?:\$[0-9][0-9,]*(?:\.[0-9]{1,2})?|\b(?:USD|USDC|DAI|ICP)\s*[0-9][0-9,]*(?:\.[0-9]{1,2})?|\b[0-9][0-9,]*(?:\.[0-9]{1,2})?\s*(?:USD|USDC|DAI|ICP)\b)/gi;

  function getVisibleText() {
    const selectors = [
      "bdi.js-issue-title",
      ".js-issue-title",
      ".js-comment-body",
      ".comment-body",
      "[data-testid='issue-body']",
      "main",
    ];
    const parts = [document.title || ""];
    selectors.forEach((selector) => {
      document.querySelectorAll(selector).forEach((node) => {
        const style = window.getComputedStyle(node);
        if (style.display !== "none" && style.visibility !== "hidden") {
          parts.push(node.innerText || node.textContent || "");
        }
      });
    });
    return parts.join("\n");
  }

  function normalize(text) {
    return String(text || "").toLowerCase().replace(/\s+/g, " ").trim();
  }

  function unique(values) {
    const seen = new Set();
    return values.filter((value) => {
      const key = value.toLowerCase();
      if (seen.has(key)) return false;
      seen.add(key);
      return true;
    });
  }

  function includesAny(text, keywords) {
    return keywords.some((keyword) => text.includes(keyword));
  }

  function detectPlatform(text) {
    for (const [platform, keywords] of platformKeywords) {
      if (includesAny(text, keywords)) return platform;
    }
    return "Unknown";
  }

  function analyze(text) {
    const normalized = normalize(text);
    const amounts = unique(text.match(amountPattern) || []);
    const platform = detectPlatform(normalized);
    const bountySignal = platform !== "Unknown" || includesAny(normalized, bountyKeywords);
    const riskFlags = [];

    if (includesAny(normalized, directPrSignals)) riskFlags.push("direct competing PR likely");
    if (includesAny(normalized, fakeSignals)) riskFlags.push("fake / test repo wording");

    Object.entries(riskGroups).forEach(([label, keywords]) => {
      if (includesAny(normalized, keywords)) riskFlags.push(label);
    });

    let recommendation = "not a bounty";
    if (bountySignal && riskFlags.some((flag) => /security|auth|payment|database|fake/.test(flag))) {
      recommendation = "avoid";
    } else if (bountySignal && (riskFlags.length || !amounts.length || platform === "Unknown")) {
      recommendation = "manual confirmation needed";
    } else if (bountySignal) {
      recommendation = "good candidate to review";
    }

    return {
      bountySignal,
      amounts,
      platform,
      riskFlags,
      recommendation,
    };
  }

  function valueClass(value) {
    if (value === "avoid") return "bountylens-bad";
    if (value === "manual confirmation needed") return "bountylens-warn";
    if (value === "good candidate to review") return "bountylens-good";
    return "bountylens-muted";
  }

  function renderPanel(result) {
    const oldPanel = document.getElementById("bountylens-panel");
    if (oldPanel) oldPanel.remove();

    const panel = document.createElement("aside");
    panel.id = "bountylens-panel";
    panel.setAttribute("aria-label", "BountyLens bounty risk panel");

    const flags = result.riskFlags.length
      ? result.riskFlags.map((flag) => `<li>${escapeHtml(flag)}</li>`).join("")
      : "<li>none detected</li>";
    const amounts = result.amounts.length ? result.amounts.join(", ") : "none detected";

    panel.innerHTML = `
      <div class="bountylens-header">
        <div>
          <div class="bountylens-title">BountyLens</div>
          <div class="bountylens-version">v${VERSION} local scan</div>
        </div>
        <button type="button" class="bountylens-close" aria-label="Close BountyLens panel">x</button>
      </div>
      <div class="bountylens-grid">
        <span>Bounty signal</span><strong>${result.bountySignal ? "yes" : "no"}</strong>
        <span>Possible amount</span><strong>${escapeHtml(amounts)}</strong>
        <span>Platform signal</span><strong>${escapeHtml(result.platform)}</strong>
        <span>Recommendation</span><strong class="${valueClass(result.recommendation)}">${escapeHtml(result.recommendation)}</strong>
      </div>
      <div class="bountylens-section">
        <div class="bountylens-section-title">Risk flags</div>
        <ul>${flags}</ul>
      </div>
      <div class="bountylens-footnote">Visible page text only. No API calls, cookies, tokens, login, comments, or PR actions.</div>
    `;

    panel.querySelector(".bountylens-close").addEventListener("click", () => panel.remove());
    document.body.appendChild(panel);
  }

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function run() {
    if (!/\/issues\/\d+/.test(window.location.pathname)) return;
    renderPanel(analyze(getVisibleText()));
  }

  run();
})();
