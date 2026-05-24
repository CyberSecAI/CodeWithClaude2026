# The thinking lever

## Executive Summary
Alexander Bricken from Anthropic's Applied AI research team discusses "test-time compute"—the principle that spending more tokens and time (reasoning) at inference time increases a model's intelligence for difficult problems. The session introduces **Adaptive Thinking** and **Effort** as the primary levers for controlling this compute. By allowing Claude to interleave thinking with tool use and plan dynamically, developers can achieve significantly higher performance on complex tasks, moving from simple chat to autonomous engineering over long horizons.

## Key Points
- **Test-Time Compute Scaling:** Like training-time compute (larger models), test-time compute (more reasoning tokens) scales intelligence. This is critical for agentic coding, complex simulations, and PhD-level reasoning.
- **Primary Levers:**
    - **Adaptive Thinking:** A scratchpad for reasoning that Claude uses dynamically. It allows the model to think *between* tool calls, mirroring human problem-solving.
    - **Effort:** A parameter (Low to Max) that defines the "budget" Claude has to solve a task. It is a more effective control than a binary thinking toggle.
- **Adaptive vs. Interleaved Thinking:** Adaptive thinking is the evolution of reasoning where Claude decides when to think, when to use a tool, and when to respond based on the specific context of the problem.
- **Effort Level Guidelines:**
    - **Extra High:** The "Pareto efficient" default for Claude Code and Claude.ai. Best balance of speed and intelligence.
    - **Max:** Reserved for the hardest autonomous engineering tasks; may have diminishing marginal returns.
    - **Low/Medium:** Use for latency-sensitive, repetitive tasks that don't require high-level reasoning (e.g., classification).
- **Large vs. Small Models:** High effort on a small model (Haiku) rarely matches the intelligence of low effort on a large model (Opus). For intelligence-bound tasks, always prioritize the larger model.
- **Task Horizon:** The "task horizon" (how long an agent can work without losing the thread) is increasing from minutes to hours and eventually days, driven by better test-time compute.

## Notable Quotes
- "Test-time compute... results in higher intelligence results."
- "A thinking toggle is actually a poor proxy... You're actually just turning off a core capability."
- "If the question... needs any intelligence at all, you're often better off using the larger model [even at low effort]."
- "The ideal world is that you set the bar in the budget... and Claude just knows how to allocate that compute appropriately."

## Takeaways
- **Never Disable Thinking:** Treat thinking as a core capability. Instead of turning it off, use **Effort** levels to manage your token budget and latency.
- **Use Evals to Find the "Sweet Spot":** Run your most difficult test cases across different effort levels to identify where accuracy plateaus.
- **Default to Extra High:** When building agents that need to solve real problems, start with the Extra High effort level.
- **Optimize for Long-Running Agents:** As models get better at test-time compute, prepare your infrastructure for agents that own high-level outcomes over hours or days.
