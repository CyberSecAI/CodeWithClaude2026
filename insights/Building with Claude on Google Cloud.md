# Building with Claude on Google Cloud

## Executive Summary
Ivan Nardini (DevRel, Google Cloud) demonstrates the seamless integration of Claude into Google Cloud's Vertex AI ecosystem. Through a live 24-minute demo, he builds and deploys a full-stack feedback application using a "Five-Role" subagent strategy. The session emphasizes the shift of Claude from a "vendor" to a native cloud component, enabling developers to leverage GCP's security, billing, and regional infrastructure while utilizing Claude Code and MCP servers for extreme automation.

## Key Points
- **Native Vertex Integration:** Claude is a native model in GCP Vertex AI. This allows for unified billing, Entra/IAM-based security, and access via regional endpoints.
- **The "Five-Role" Subagent Strategy:** A single orchestrator spawns specialized agents to parallelize the SDLC:
    - **PM:** Specs and acceptance criteria.
    - **Designer:** UI components and Tailwind layout from wireframes.
    - **Engineer:** Backend routes, frontend logic, and database schema.
    - **Security:** Vulnerability review and IAM configuration.
    - **QA:** End-to-end test execution.
- **Infrastructure as Code (GCP MCP):**
    - The **Google Cloud MCP server** allows Claude to interact directly with GCP services.
    - Claude can provision Cloud Run, manage Cloud SQL, and tail logs as native tool calls.
- **Markdown "Skills":** Use project-specific markdown files (e.g., `deploy-convention.md`) to maintain standards across the five parallel subagents.
- **ADC Setup:** Using Application Default Credentials (ADC) to automatically detect project and regional context for Claude Code.

## Notable Quotes
- "Claude stopped being a vendor; it became a line item on a bill you were already paying."
- "The core of the demo isn't the app—it's the subagent strategy that parallelizes the human brain."
- "What's better than me running into the bug first? Us having automation in place to catch it closer to the source."

## Takeaways
- **Deploy via Vertex AI:** Move your production Claude workloads to Google Cloud Vertex AI for better enterprise governance and regional compliance.
- **Adopt the "Five-Role" Playbook:** When building new features, prompt Claude Code to spawn specialized subagents for PM, Design, Dev, Security, and QA to ensure a high-quality "Shift Left" outcome.
- **Install the GCP MCP Server:** Give your agents the ability to manage their own cloud infrastructure and debug live environments using Cloud Logging tools.
- **Standardize with Skills:** Check your deployment and testing policies into your repo as Markdown files so all subagents follow the same "Golden Rules."
