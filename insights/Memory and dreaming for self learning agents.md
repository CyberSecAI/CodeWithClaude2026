# Memory and dreaming for self learning agents

## Executive Summary
Anthropic introduces "Memory" and "Dreaming" as foundational building blocks for agents to learn and improve over time. Memory allows agents to carry forward learnings across sessions, while Dreaming is an out-of-band background process that optimizes and curates organizational memory globally across all agents.

## Key Points
- **Memory Evolution:** Moves from session-specific tools (Claude.md) to a shared, file-system-based architecture that Claude naturally understands.
- **Enterprise Controls:** Includes version control, audit trails, and optimistic concurrency control to prevent data conflicts in multi-agent systems.
- **Memory Tiers:** Supports hierarchical memory, such as read-only organization-wide knowledge (policies, runbooks) and read-write granular task stores.
- **Dreaming Defined:** A decoupled batch process that analyzes transcripts, identifies patterns in mistakes or inefficiencies, and refines memory snapshots.
- **Performance Impact:** Early adopters saw significant results, including a 97% decrease in first-pass errors for Rakuten and a 6x increase in completion rates for Harvey.
- **Decoupled Architecture:** Dreaming runs out-of-band, avoiding latency in the agent's hot path and preventing trade-offs between task completion and memory quality.

## Notable Quotes
- "Memory lets agents learn. It lets agents carry forward learnings from their previous tasks."
- "Dreaming is the bridge between memory as we know it today and organization scale memory and knowledge."
- "Let it cook." (Referring to letting Claude manage its own memory structure).
- "Sharing memory... raises the floor for every agent. And dreaming raises it even further."

## Takeaways
- Implement hierarchical memory stores (e.g., read-only org policy vs. read-write task memory) to provide agents with consistent guidance.
- Use the Dreaming API to trigger background optimizations after sessions or on a schedule to improve agent reliability automatically.
- Leverage versioning and attribution in memory to maintain transparency and auditability for production agents.
