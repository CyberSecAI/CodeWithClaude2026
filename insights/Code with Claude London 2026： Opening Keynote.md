# Code with Claude London 2026: Opening Keynote

## Executive Summary
The keynote from Code with Claude London 2026 highlights the collapsing distance between an idea and a shipped product. Boris Churney and the Anthropic team discuss the exponential growth of Claude's capabilities—from drafting git commits to autonomous engineering. Key announcements include Claude Managed Agents features (self-hosted sandboxes, MCP tunnels), new Cloud Code interfaces (Desktop app, Agent view), and "Routines"—a higher-order prompt primitive that allows Claude to be proactive and "always-on."

## Key Points
- **Collapsing the Distance:** Modern coding is shifting from complex configuration (compilers, type checkers) to natural language problem description, restoring the "tinkering" feel of early computing.
- **Model Evolution:**
    - **Task Horizon:** Reliable autonomous work has increased from minutes to hours, with the goal of "continuous" operation.
    - **Capability Jumps:** Progress from code proficiency (Opus 3) to computer use (Sonnet 3.5) and complex autonomous engineering with high judgment (Opus 4.7).
- **Claude Platform & Managed Agents:**
    - **Advisor Strategy:** Splitting execution (small model) from advising (large model) to achieve frontier quality at lower costs.
    - **Self-hosted Sandboxes:** Run agent work on private infrastructure (Daytona, Cloudflare, Vercel, Modal).
    - **MCP Tunnels:** Secure access to internal, firewalled data sources.
- **Cloud Code Innovations:**
    - **New Interfaces:** Cloud Code Desktop, Agent View in CLI, and mobile apps (iOS/Android) for coding on the go.
    - **Routines:** Async automations that run on schedules or webhooks, allowing Claude to "prompt itself" to solve issues.
    - **CI Autofix:** Proactively fixes review comments, CI flakes, and merge conflicts to ensure PRs stay green.
- **Real-world Impact:**
    - **Spotify:** Automating migrations across thousands of repos, merging 1,000+ PRs/month.
    - **Mercado Libre:** Modernizing 9,000+ apps and aiming for 90% autonomous coding in the PR loop.
    - **Binty:** Reducing foster care licensing by 20 days.

## Notable Quotes
- "The distance between I have an idea and it runs just kept getting longer. What's happening now is that distance is collapsing again."
- "The default isn't I'm going to prompt Claude code. The default is now I'm going to have Claude prompt Claude Code."
- "Scaffolding... can hold Claude back. Claude is intelligent and resourceful... and can often get further with generalized primitives."
- "You need to build for emerging capabilities, not just what works today."

## Takeaways
- **Build for the Future:** Design system architectures that are ready to absorb the next jump in model intelligence.
- **Shift to Async:** Move from manual, reactive prompting to asynchronous workflows using **Routines** and **CI Autofix**.
- **Optimize for Cost:** Use the **Advisor Strategy** to get frontier model performance using smaller, cheaper executors.
- **Focus on Goals:** As models handle implementation, developers should shift focus to defining high-level goals and exercising judgment.
