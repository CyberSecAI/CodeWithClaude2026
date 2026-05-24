# What legal agents inherit from coding agents: Lessons from Legora

## Executive Summary
Jakob Emmerling (Staff Engineer, Legora) and Jacob Lauritzen (CTO, Legora) share how principles from the AI coding agent revolution (Claude Code, Cursor) were successfully applied to the legal industry. The core insight is that legal work shares the same "structural DNA" as software engineering: text-based precision, reusable patterns (clauses/libraries), and a rigorous review culture. By "inheriting" and adapting patterns like Read-Edit-Verify loops, sandboxing, and linters, Legora is building agents that move beyond simple Q&A to autonomous legal matter management.

## Key Points
- **Structural DNA:** Law and Coding both rely on precision (commas vs. semicolons), reusable templates (clauses vs. libraries), and version control (matter files vs. codebases).
- **The Patterns of Inheritance:**
    - **Reuse (1:1):** Patterns like **Planning & To-Dos**, **Sandboxing**, and **Human-in-the-Loop** checkpoints translate directly.
    - **Translate (Adaptation):**
        - **Read-Edit-Verify:** Legora converts `.docx` files to a flat, text-based intermediate representation so agents can apply surgical patches rather than rewriting entire documents.
        - **Legal Linters:** Automated checks for broken cross-references, inconsistent definitions, and deviations from a firm's "Golden Playbooks."
    - **Invent (Vertical-Specific):** **Bulk Table Review** for thousands of documents (due diligence) where agents present structured data grids for human verification.
- **Verification Proxies:** Since law has no "compiler," Legora uses "Golden Contracts" as a proxy—testing if a new draft aligns with the logic of a historically proven document.
- **Elicitation vs. Autonomy:** High-trust tasks (checking definitions) are automated, while low-trust/high-complexity tasks (litigation strategy) require the agent to stop and "elicit" the user's risk profile before proceeding.

## Notable Quotes
- "Legal work is effectively one cycle behind software development... we are inheriting their DNA."
- "A comma in a contract is as dangerous as a semicolon in a codebase."
- "Getting out of Claude's way is the new senior engineering skill... and soon the new senior associate skill."

## Takeaways
- **Apply the "Read-Edit-Verify" Loop:** Don't ask agents to rewrite entire entities (files or contracts). Ask for surgical "diffs" or patches to minimize drift and hallucinations.
- **Build Domain Linters:** Create automated checks for your industry's specific "syntax" (e.g., cross-references in law, logic gates in finance).
- **Use "Golden Standards" for Eval:** When a programmatic "compiler" isn't available, use your best historical work as the benchmark against which agents must evaluate their new outputs.
- **Bridge the Trust Gap via Elicitation:** Design your agents to stop and ask for "intent" (risk tolerance, tone, strategy) when entering high-stakes logic paths.
