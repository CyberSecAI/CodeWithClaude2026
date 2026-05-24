# Picking the right model

## Executive Summary
Lucas from Anthropic's Applied AI team discusses the strategic process of selecting the optimal Claude model for specific business use cases. Moving beyond generic benchmarks, the session advocates for building custom, data-driven evaluations (evals) that balance quality, latency, and cost. By leveraging features like adaptive thinking, effort parameters, prompt caching, and rigorous context engineering, developers can shift the efficiency frontier—often finding that larger models like Opus can be more cost-effective per successful outcome than smaller models like Haiku or Sonnet.

## Key Points
- **The Three Pillars of Model Selection:**
    - **Quality:** Task completion rate and accuracy.
    - **Latency:** Time-to-response, critical for user experience.
    - **Cost:** Total expenditure per *successful outcome*, not just per token.
- **Custom Evals vs. Public Benchmarks:** Public benchmarks are directional but rarely match heterogeneous production workloads. A small, well-designed private eval is the most reliable tool for decision-making.
- **Eval Design (The "Maths Exam" Heuristic):**
    - **The Working:** Inspecting the intermediate steps (e.g., tool calls, research) is as important as the final outcome, especially for agentic tasks. Use LLM-as-a-judge for robust step validation.
- **Dials for Fine-Grained Control:**
    - **Adaptive Thinking:** A scratchpad for complex reasoning.
    - **Effort:** A parameter that tells Claude how much work to put into a task, allowing trade-offs between accuracy and token volume.
- **Efficiency Strategies (Shifting the Frontier):**
    - **Prompt Caching:** Reduces input costs by 90%. Best practice involves "append-only" message arrays and keeping system prompts immutable (no dynamic timestamps).
    - **Context Hygiene:** Simplifying API responses (e.g., JSON to Markdown) and deduplicating data can reduce token usage by 60-70% while *increasing* accuracy.
- **Counterintuitive Findings:** More intelligent models (Opus) often reach success in fewer turns and with fewer total tokens than smaller models, potentially making them faster and cheaper per successful task.

## Notable Quotes
- "The right model... is the one that is cheapest per successful outcome."
- "Thinking is giving Claude a scratchpad to think before it acts."
- "People spend too much time thinking about super complex multi-agent orchestration... and not enough time doing the simple thing that works: good context hygiene."
- "The closer you can get to the raw data, very much the better."

## Takeaways
- **Invest in Evals:** Building a reference set of production-representative tasks is the highest leverage use of developer time.
- **Read Transcripts:** Regularly inspect raw traces to identify "silent saturation" or infrastructure failures masked as model errors.
- **Maximize Prompt Caching:** Target 80-90% hit rates to unlock frontier intelligence (Opus) at Sonnet-level pricing.
- **Clean the Context:** Treat Claude like a human—provide clean, simplified, and deduplicated data to improve reasoning and reduce overhead.
