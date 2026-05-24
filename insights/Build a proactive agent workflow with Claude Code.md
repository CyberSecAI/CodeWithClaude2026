# Build a proactive agent workflow with Claude Code

## Executive Summary
This session introduces "routines" in Claude Code, a feature that transforms Claude from a reactive tool into a proactive teammate. By automating tasks on a schedule or event-based triggers (such as GitHub events or webhooks), routines allow agents to handle infrastructure, data persistence, and authentication independently of a local machine.

## Key Points
- **Routines Overview:** Automation that kicks off remote Claude Code sessions based on prompts, repos, connectors, and triggers.
- **Always Available:** Runs on managed infrastructure, eliminating the need for local hosting or persistent laptop connections.
- **Customizable Triggers:** Supports time-based schedules (cron-like) and event-based triggers (GitHub events, custom webhooks).
- **Steerability:** Sessions are interactive and can be monitored, steered, or resumed via web, CLI, or desktop.
- **Real-world Use Case:** Automating documentation updates at Anthropic by diffing source code against documentation repos weekly or on PR merges.
- **Agent-on-Agent Review:** Using one routine to generate content and another to critique/review it.

## Notable Quotes
- "Coding agents shouldn't wait for you to press enter to get started."
- "A teammate notices when something breaks and does something about it."
- "Whatever context Claude has, that's the ceiling of how successful Claude will be."
- "Proactive agents beat reactive agents."

## Takeaways
- Use `/schedule` in Claude Code to set up your first routine and move from reactive to proactive workflows.
- Automate repetitive "teammate" tasks like documentation updates, deploy verification, or backlog prioritization.
- Invest in "agent-on-agent" review patterns to ensure quality and reliability in automated outputs.
