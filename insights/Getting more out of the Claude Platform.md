# Getting more out of the Claude Platform

## Executive Summary
Punit Shah (Product Manager, Anthropic) discusses the three pillars of the Claude Platform: cutting costs, managing context, and boosting intelligence. The session highlights the massive financial impact of **Prompt Caching** (90% cost reduction) and the strategic use of **Advisor Strategy** to achieve frontier-level intelligence at a fraction of the cost. The talk emphasizes a data-driven approach to agent development, using console analytics to optimize cache hit rates and context compaction.

## Key Points
- **Prompt Caching:**
    - Process input tokens once and reuse them across subsequent turns.
    - **90% Discount:** Significant cost savings as tokens aren't re-processed.
    - **Best Practices:** Place static content (system prompts, docs) at the beginning. Avoid dynamic data (like timestamps) in the system prompt.
- **Context Management for Agents:**
    - Use tools to search large datasets instead of stuffing everything into the context window.
    - Implement context compaction strategies to keep long-running agents lean and efficient.
- **The "Advisor" Strategy:**
    - Use a smaller model (Haiku/Sonnet) for the bulk of task execution.
    - Bring in a larger model (Opus) as an "advisor" for high-complexity reasoning steps or final quality checks.
- **Cache Analytics:**
    - Use the Anthropic Console to monitor cache hit rates.
    - Debug cache misses to identify where dynamic data is breaking the prefix.
- **Production Readiness:** The session highlights that while many build agents, few have successfully optimized them for production-level quality, cost, and speed.

## Notable Quotes
- "The first reason [to care about prompt caching] is you get a 90% discount because we're not reprocessing them."
- "A common error I see is people putting a timestamp into the system prompt... that's useful, but it breaks your cache every single time."
- "This session is about... building a real business and real products that deliver for your users."

## Takeaways
- **Target 80-90% Cache Hit Rate:** Redesign your prompt structures to ensure the largest part of your context (docs, codebase snapshots) remains static and prefix-cacheable.
- **Audit System Prompts:** Remove any frequently changing variables (dates, times, user session IDs) from the beginning of your prompts.
- **Implement the Advisor Strategy:** Reduce costs by 50-70% by using Haiku for boilerplate and Opus only for the "hard" reasoning.
- **Use Console Analytics:** Regularly check the Anthropic Console to identify "papercut" costs caused by inefficient context management.
