# Build a production-ready agent with Claude Managed Agents

## Executive Summary
This session provides a technical deep dive into "Claude Managed Agents," a set of API endpoints that provide production-ready primitives for building agentic applications. Instead of managing the agent loop, sandboxing, and state transitions manually, developers can use these managed building blocks (Agents, Environments, Sessions, and Events) to scale applications quickly while maintaining high observability through the Anthropic developer console.

## Key Points
- **Core Primitives:**
    - **Agent:** A template defining system prompts, skills, tools (like bash or web search), and MCP servers. It handles permission controls (e.g., auto-execute vs. human-in-the-loop approval).
    - **Environment:** Defines the sandbox where Claude operates (network access, pre-installed packages). Supports self-hosted sandboxes (Cloudflare, Modal, Vercel).
    - **Session:** An ongoing conversation thread. Can pre-load GitHub repos or files into the container.
    - **Events:** The stream of communication including user inputs, agent actions (tools, messages), and system state transitions.
- **Advanced Features:**
    - **Outcomes:** A mode where Claude iterates against a provided "rubric" or spec, checking and criticizing its own work until the goal is satisfied.
    - **Multi-agent Coordination:** Claude can spawn specialized sub-agents with their own context windows to handle specific sub-tasks (e.g., one for financial analysis, another for macro trends).
    - **Credential Vaults:** Securely stores MCP authentication tokens, injecting them into tool calls without Claude ever seeing the raw secrets.
    - **Memory Stores:** Allows Claude to read and write persistent memories across different sessions, enabling long-term learning and context.
    - **Observability:** A specialized developer console for live debugging, monitoring tool call performance, and inspecting multi-agent interaction spans.
- **Security & Networking:**
    - **Self-hosted Sandboxes:** Allows agents to run within a developer's own VPC or perimeter.
    - **MCP Tunnels:** Securely connects private, internal data sources to Claude without exposing them to the public internet.

## Notable Quotes
- "Claude managed agents... give you access to scaled-ready, production-ready agents and all of the primitives around it."
- "You can build your own Claude with Claude."
- "Outcomes... is a really great way to set up your agents for success."
- "Agents are versioned, so if you ever feel like you made an update that you're not happy with... you can always go back."

## Takeaways
- Transition from manual agent loop management to "Claude Managed Agents" to offload infrastructure, storage, and state management.
- Use **Credential Vaults** and **MCP Tunnels** to integrate sensitive or private company data securely.
- Leverage the **Developer Console** for real-time monitoring of complex multi-agent workflows.
- Implement **Outcomes** to ensure high-quality, rubric-aligned results through automated iterative refinement.
