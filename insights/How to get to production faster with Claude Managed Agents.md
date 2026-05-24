# How to get to production faster with Claude Managed Agents

## Executive Summary
Michael and Harrison from Anthropic discuss the evolution of Claude's capabilities and the shift toward "Claude Managed Agents." As model intelligence increases, infrastructure (context management, sandboxing, observability) becomes the primary bottleneck. Managed Agents provide a production-ready harness that handles these complexities out of the box, allowing developers to focus on high-level goals and task completion rather than manual tool orchestration. The session also features a panel with infrastructure partners (Cloudflare, Daytona, Modal, Vercel) discussing the importance of self-hosted sandboxes and secure networking for agentic systems.

## Key Points
- **Infrastructure as the Bottleneck:** For long-running, autonomous agents (multi-hour or multi-day tasks), traditional "prompt + tool use" is insufficient. Robust infrastructure is required to manage state, memory, and security.
- **Core Managed Agent Primitives:**
    - **Agent Definition:** A bundle of system prompt, model, skills, tools, and permissions (the agent's identity).
    - **Environment:** The sandbox (computer access) with networking allow-lists and pre-installed packages.
    - **Session:** A stateful conversation log (event stream) of user and agent actions.
- **Event Stream Categories:**
    - **User Events:** Text, images, docs, interrupts (to steer Claude), and outcome definitions.
    - **Agent Events:** Tool execution, messages, and multi-agent coordination.
    - **Session Events:** Lifecycle status (idle, running, error recovery).
    - **Span Events:** Tracking long-running processes like document generation.
- **Advanced Features:**
    - **Multi-agent Orchestration:** Spawning sub-agent threads with independent context windows for task delegation.
    - **Outcomes:** Defining a goal rubric for iterative refinement until success.
    - **Dreaming:** Async reflection over thousands of sessions to improve long-term memory.
    - **Self-hosted Sandboxes:** Bringing private compute (via Cloudflare, Daytona, Modal, Vercel) to keep data within a private VPC.
    - **MCP Tunnels:** Securely exposing internal data sources to Claude without public internet access.
- **Partner Insights (Panel):**
    - **Scalability:** The need to spin up hundreds of thousands of sandboxes instantly (Modal) or use lightweight "isolates" (Cloudflare) to handle massive future agent volume.
    - **Identity & Security:** The challenge of assigning and propagating identity down a chain of agents to ensure proper data access (Cloudflare/Vercel).
    - **Human Emulation:** Using sandboxes to allow agents to interact with legacy Windows applications or any digital task a human can perform (Daytona).

## Notable Quotes
- "The bottleneck towards increasing capabilities is really the infrastructure around these models and not so much the intelligence for them."
- "Everyone now has a chief of staff... doing market research, trying to understand the product that they're working on."
- "Anything that a human can do digitally... you can now have an agent do if you give it a sandbox."

## Takeaways
- Offload the "undifferentiated heavy lifting" of agent infrastructure (memory, storage, sandboxing) to **Claude Managed Agents**.
- Use **Self-hosted Sandboxes** to run agents on private data or within specific regulatory perimeters.
- Leverage **Multi-agent Orchestration** to break down large, complex projects into parallelizable sub-tasks.
- Integrate **MCP Tunnels** to connect Claude to internal legacy systems and private data warehouses securely.
