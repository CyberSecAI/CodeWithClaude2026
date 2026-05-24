# Build AI agents using Claude in Microsoft Foundry

## Executive Summary
Marlene Mangami from Microsoft introduces Microsoft Foundry as a unified platform for building, deploying, and scaling AI agents using Claude models. The session emphasizes the shift from single-turn chat to agentic systems that plan, reason, and take action. Using a hands-on "Sparkles Cupcake Shop" workshop, the team demonstrates how to deploy Claude Sonnet 4.6 in Foundry, connect it to local development environments via VS Code, and use the Model Context Protocol (MCP) to give agents real-world capabilities.

## Key Points
- **Microsoft Foundry Overview:** A unified AI platform integrating models (like Claude), agent services, tools, and enterprise features (security, observability, governance).
- **Agentic Challenges:** Modern agents must handle multi-step reasoning, long context understanding, reliability, and external tool connectivity.
- **Claude in Foundry Benefits:**
    - **Reasoning:** Best-in-class planning and long-context understanding using Claude models (e.g., Sonnet 4.6, Opus 4.7).
    - **Orchestration:** Seamless agent creation and tool access within the platform.
    - **Enterprise Ready:** Built-in security, compliance, and Entra ID integration.
    - **Velocity:** Faster production cycles with evaluation, observability, and monitoring tools.
- **Hands-on Workshop (Sparkles Cupcakes):**
    - **Deployment:** Deploying Claude via the Foundry Model Catalog.
    - **Playground:** Testing system prompts and personas in the Foundry web UI.
    - **Local Integration:** Using the Microsoft Agent Framework (Python/TypeScript) to connect local code to Foundry endpoints.
    - **MCP Integration:** Connecting an MCP server to provide the agent with resources (inventory), prompts (instructions), and tools (ordering functions).
    - **End-to-End Workflow:** The agent registers customers, checks real-time inventory, and processes orders through a live dashboard.

## Notable Quotes
- "Microsoft Foundry is our unified platform for building AI applications and agents at scale."
- "You can't just rely on the models getting better. We also need systems to be able to actually have those models or that intelligence executed."
- "Opus 4.7 is my current daily driver... excellent at planning and working with long context."
- "MCP is an open standard for letting AI agents talk to external systems."

## Takeaways
- Use Microsoft Foundry to transition from prototypes to production enterprise environments with built-in security and observability.
- Leverage the **Microsoft Agent Framework** for high-level orchestration of Claude-powered agents.
- Adopt **MCP (Model Context Protocol)** to standardize how agents interact with existing company data and APIs.
- Utilize Foundry's **evaluation and monitoring tools** to ensure agent reliability before deployment.
