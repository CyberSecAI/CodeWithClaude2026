# The prompting playbook

## Executive Summary
Margot Vanlar from Anthropic's Applied AI team discusses the evolution of prompting as a core engineering skill. The session focuses on two scenarios: maintaining/migrating existing prompts and building new agentic use cases from scratch. Through rigorous evaluation and iterative refinement, developers can debug failure modes (like hallucinations or information withholding) and optimize performance by balancing model capability, prompting structure, and agentic loops.

## Key Points
- **Foundational Principles:**
    - **Evaluations are Mandatory:** Use an eval suite with control cases (should always pass), edge cases (historical failures), and hand-off cases (when to call a human).
    - **General Hygiene:** Remove redundant instructions and role-playing (e.g., "you are a human"). Use **XML tags** to structure the prompt into role, guidelines, policy, and data.
- **Prompt Maintenance & Migration:**
    - **Structure Matters:** If you can't distinguish between policy and tone in a prompt, the model likely can't either. XML tags provide clear boundaries.
    - **Clean the "Scaffold":** Old "patches" for previous models (e.g., "never give specific numbers") may cause modern models to withhold valid information. Version control your prompts to track why instructions were added.
    - **Instructions vs. Capability:** Telling a model to "do a good job" on math doesn't make it better at math. **Give it a tool** (e.g., a calculator) instead.
    - **Balanced Trade-offs:** When giving negative constraints (e.g., "avoid escalation"), provide the counter-risk (e.g., "but prioritize customer trust over cost") to enable better judgment.
- **Building from Zero to One (Agentic Design):**
    - **Hill Climbing:** Start simple. If a smaller model fails, try a larger model (Opus) or enable **Adaptive Thinking**.
    - **Agentic Loops (Generate-Evaluate-Repair):** For complex tasks like scheduling, splitting one large prompt into three independent steps (Draft, Critique, Fix) is often more efficient and reliable than a single-turn prompt.
    - **Soft Constraints:** Agentic loops allow for runtime flexibility (e.g., "Harry doesn't like working with Sally") without rewriting programmatic logic.

## Notable Quotes
- "Instructions don't add capability."
- "If you're reading a prompt and you can't tell guidelines from policy... most likely the model isn't able to either."
- "The model can withhold information that it actually has access to... likely a result of a patch introduced for a previous model."

## Takeaways
- **Standardize with XML Tags:** Always use XML tags to improve instruction following and maintainability.
- **Use Tools for Deterministic Tasks:** Reserve the model for reasoning and use tools for execution (math, data retrieval).
- **Chain Simple Prompts:** For complex workflows, use a critique/repair loop to achieve high accuracy with lower-latency models (Sonnet).
- **Version Control Instructions:** Document why specific prompt constraints exist to avoid "bloat" and overfitting as models improve.
