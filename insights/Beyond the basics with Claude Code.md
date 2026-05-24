# Beyond the basics with Claude Code

## Executive Summary
Daisy Hollman (MTS, Anthropic) and Boris Cherny (Head of Claude Code) lead a workshop on advanced workflows for Claude Code. The session shifts the perspective from "unlimited context" to "rigorous context hygiene," emphasizing that the agent's effectiveness is determined by the quality, not the quantity, of information provided. Key takeaways include the implementation of `CLAUDE.md` for project memory, the creation of self-improving skills, and the adoption of agent-optimized verification tools.

## Key Points
- **The Context Strategy:** The context window is a "fixed box." The primary engineering task is selecting the most relevant files and data to fit inside it. FLOODING the agent with the entire codebase leads to performance degradation.
- **Institutional Memory (`CLAUDE.md`):**
    - Place this file in the project root.
    - Include: Build/test commands, coding style, architectural principles.
    - **The Golden Rule:** Every time the agent makes a mistake, add a rule to `CLAUDE.md` to prevent it from happening again.
- **Skills vs. Workflows:**
    - **Workflows:** Linear, input-to-output processes.
    - **Skills:** Dynamic, context-aware capabilities that allow agents to "document themselves" and improve over time.
- **The Agentic Loop:**
    1. **Gather Context:** Determine what's needed.
    2. **Take Action:** Edit files/run commands.
    3. **Verify:** Use tests/linters to confirm success.
    4. **Iterate:** Fix failures and loop back.
- **Agent-Optimized Tooling:** Modern linters and compilers were built for humans. Future tooling should provide structured, high-signal error messages designed specifically for agent parsing and auto-fixing.
- **Advanced Features:**
    - **Git Worktrees:** Native support for isolating feature work.
    - **Plan Mode:** Compile a read-only plan before any file modifications.
    - **Remote Control:** Monitor and provide input to Claude Code from mobile notifications.

## Notable Quotes
- "The context window is a fixed box... the real leverage comes from curating what goes into it."
- "We can write code 10 times faster, we should throw out code 10 times faster as well."
- "Getting out of Claude's way is the new senior engineering skill."

## Takeaways
- **Implement `CLAUDE.md` immediately:** Treat it as your agent's "onboarding guide" and update it iteratively after every bug fix.
- **Shift to "Verification-First" Coding:** Spend less time on the implementation prompt and more time on the automated verification (tests/lints) that tells the agent when it's finished.
- **Use Plan Mode for Complex Refactors:** Always force the agent to "think out loud" and list the files it will touch before it starts writing.
- **Adopt "Self-Improving" Skills:** Instruct your custom skills to log their own blockers and suggest updates to their own instructions.
