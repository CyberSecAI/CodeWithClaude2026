# Building AI-native at enterprise scale: monday.com, Doctolib, and Delivery Hero

## Executive Summary
Engineering leaders from monday.com (VP Eng Dikaia Chatziefstathiou), Doctolib (CEO Stanislas Niox-Chateau), and Delivery Hero (CTO Christian Hardenberg) discuss the transition from "AI features" to "AI-native" enterprise architecture. The session explores how these companies use Claude to reduce developer onboarding time, automate complex medical documentation, and manage global logistics. The common thread is the move toward autonomous agents and the need for centralized AI governance platforms to manage cost, security, and performance at scale.

## Key Points
- **monday.com (Dikaia Chatziefstathiou):**
    - **Developer Productivity:** An internal "AI Assistant" reduces onboarding time by providing instant context on massive codebases.
    - **AI-Native Architecture:** Moving beyond simple features to architectures where Claude is a core part of the product logic.
    - **Governance:** Implementing prompt versioning and evaluation frameworks to manage hundreds of developers building AI features simultaneously.
- **Doctolib (Stanislas Niox-Chateau):**
    - **Medical Documentation:** Using Claude to summarize consultations and automate administrative tasks, allowing doctors to focus on patients.
    - **Safety & Trust:** A strict "Human-in-the-Loop" approach where AI suggests but medical professionals always validate.
    - **Privacy:** Maintaining rigorous healthcare compliance (GDPR/HIPAA) in a medical context.
- **Delivery Hero (Christian Hardenberg):**
    - **Logistics Optimization:** Using AI to optimize delivery networks across diverse regions and languages.
    - **Agentic Support:** Transitioning from simple chatbots to sophisticated agents that resolve complex refund/delivery issues autonomously.
    - **Operational Efficiency:** Moving from manual business rules to adaptive, agent-driven workflows.
- **Enterprise Themes:**
    - **Centralized AI Platforms:** The need for internal platforms to manage model costs and security across many teams.
    - **Shift to Autonomy:** All three companies are moving from "Copilots" (suggestions) to "Agents" (end-to-end task completion).

## Notable Quotes
- "We're moving from AI as a feature to AI as a foundational component of our architecture."
- "The primary skill for a 2026 engineer is no longer syntax; it's being the 'Grader-in-Chief' of agentic output."
- "Trust is built when the agent suggests and the human validates—never when the agent acts in a black box."

## Takeaways
- **Build an Internal "AI Knowledge" Assistant:** Reduce developer toil by using Claude to index your internal docs and codebases for instant context.
- **Implement a "Human-in-the-Loop" Validation Layer:** Especially in high-stakes industries (Health, Finance, Logistics), ensure agents provide suggestions that require explicit human approval before execution.
- **Centralize AI Governance:** Create a "Platform" team responsible for prompt versioning, cost monitoring, and model evaluation across the entire organization.
- **Target Long-Horizon Tasks:** Identify "asynchronous" workflows (like medical summaries or logistics routing) where agents can work in the background to free up human capacity.
