(function () {
  "use strict";

  const promptText = `/goal
Review the current GitHub issue as a bounty candidate.

Safety boundaries:
- Read only public issue/repository content.
- Do not read cookies, keychain, password manager, private tokens, or credentials.
- Do not process KYC, payment, withdrawal, wallet, crypto, auth, security, or database migration tasks.
- Do not comment, claim a bounty, or create a PR.
- Produce a concise candidate review with bounty signal, fake-bounty risk, competing PR risk, testability, and next recommendation.`;

  const button = document.getElementById("copyPrompt");
  const status = document.getElementById("copyStatus");

  async function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      await navigator.clipboard.writeText(text);
      return;
    }
    const textarea = document.createElement("textarea");
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand("copy");
    textarea.remove();
  }

  button.addEventListener("click", async () => {
    try {
      await copyText(promptText);
      status.textContent = "Prompt copied.";
    } catch (error) {
      status.textContent = "Copy failed. Open the prompts folder instead.";
    }
  });
})();
