# The Claude Code roadmap

## Executive Summary
Dickson Tsai (Anthropic) outlines the strategic roadmap for Claude Code, focusing on two primary pillars: **Developer Experience (DX)** and **Autonomy**. The roadmap shifts Claude Code from an interactive CLI tool to an autonomous agent capable of "long-horizon" work—handling complex, multi-day engineering tasks independently. Key future capabilities include **Auto Mode** for smart permissions, **Routines** for asynchronous automation, and a **Coordinator Mode** for multi-agent orchestration.

## Key Points
- **Developer Experience (DX) Enhancements:**
    - **Auto Mode:** An internal classifier that makes permission decisions on behalf of the user, suppressing manual prompts for "safe" actions and only interrupting for high-risk changes.
    - **AutoMemory:** An automated project directory (`memory.md`) that accumulates knowledge (build commands, debugging insights, preferences) so the agent never starts from a blank slate.
- **Pushing Toward Autonomy:**
    - **Routines (Research Preview):** Reusable automation configurations (Prompt + Repo + Connectors) that can be triggered by webhooks or cron schedules.
    - **Coordinator Mode:** A multi-agent architecture where a lead Claude agent breaks down complex goals and delegates them to specialized sub-agents.
    - **Scheduled Remote Agents:** The ability to run long-running sessions on Anthropic's hosted infrastructure, allowing agents to "cook" on a problem while the developer is away.
- **Ecosystem & Infrastructure:**
    - **Claude Agent SDK:** Releasing the underlying building blocks of Claude Code to allow developers to build their own sophisticated, file-writing agents.
    - **Hosted Code Execution:** Providing Claude with a managed server-side sandbox for running tests and scripts, removing the need for local VM configuration.
- **The "Expert" Learning Path:** A 5-tier roadmap for developers to master the tool, moving from basic installation to multi-agent coordination and custom skill development.

## Notable Quotes
- "We want to make Claude Code 'nicer to live in' as you spend more of your day within the tool."
- "The roadmap shifts Claude from an interactive tool to an autonomous operator capable of long-horizon work."
- "Getting out of Claude's way is the new senior engineering skill."

## Takeaways
- **Prepare for "Async" Engineering:** Start designing your workflows around the upcoming **Routines** feature—identify repetitive tasks (dependency updates, bug triage) that you want to delegate to a scheduled agent.
- **Implement `memory.md` manually today:** Even before AutoMemory is fully native, start a project-specific memory file to ground your agent in your specific build and test conventions.
- **Explore the Agent SDK:** Once released, use the Claude Agent SDK to build specialized agents for your company's unique domain (e.g., custom security audit agents or API migration agents).
- **Master Multi-Agent Coordination:** As Coordinator Mode arrives, focus on your ability to break down monolithic tasks into independent sub-tasks that can be handled in parallel by agent teams.
