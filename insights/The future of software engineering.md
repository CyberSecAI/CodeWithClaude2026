# The future of software engineering

## Executive Summary
Boris Cherny (Head of Claude Code) and Jeremy Hadfield (Anthropic) explore the profound shift from "writing" code to "verifying" it. The session details how the role of a software engineer is evolving into that of an **Agent Orchestrator**, where the primary skill is building robust verification systems (automated tests, linting, rubrics) rather than manual syntax production. Key announcements include **Claude Dreams** for autonomous architectural reflection and **Outcomes** for rubric-based self-evaluation by agents.

## Key Points
- **The "Let it Cook" Philosophy:** Moving from "AI as a co-pilot" to "AI as an autonomous teammate." The goal is to get out of the agent's way and allow it to work continuously on long-horizon tasks.
- **Verification over Creation:** About half the audience reported shipping PRs written entirely by Claude, with some shipping without reading the code at all. This highlights the critical importance of **Verification Systems**.
- **Claude Dreams (Research Preview):** A background process where Claude "sleeps" on a codebase, reviewing past sessions and identifying patterns or architectural debt to optimize its future memory.
- **Outcomes (Public Beta):** A rubric-based grading system where developers define "what good looks like" for a task. Claude evaluates its own output against this rubric before submitting a PR.
- **Multi-Agent Orchestration:** Lead agents can now spawn and manage sub-agents to handle parallel work streams (e.g., one agent coding, another writing unit tests).
- **Routines:** Scheduled, asynchronous automations that allow Claude to perform background maintenance (dependency updates, doc syncing) without human intervention.
- **The Collapsing Gap:** The distance between a human with an idea and a working product is rapidly approaching zero.

## Notable Quotes
- "The default isn't 'I'm going to prompt Claude' — the default is now 'I'm going to have Claude prompt itself.'"
- "Software is becoming something you ask for instead of something you hire for."
- "Getting out of Claude's way is the new senior engineering skill."
- "You have to be the 'Grader-in-Chief' for your own work."

## Takeaways
- **Shift to "Async" Engineering:** Design your workflows around agents that can "cook" on a problem for hours or days without constant human steering.
- **Invest in Verification Infra:** Your highest leverage activity is no longer writing the implementation, but writing the **Tests and Rubrics** that define a successful outcome.
- **Utilize Claude Dreams:** Allow the agent to periodically reflect on your codebase to identify architectural rot and suggest "dreamed" refactors.
- **Standardize with Outcomes:** Use the **Outcomes** feature to codify your team's definition of "Quality" so agents can self-correct before they ever reach a human reviewer.
