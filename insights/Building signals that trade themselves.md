# Building signals that trade themselves

## Executive Summary
Man Group shares their journey of integrating AI into systematic trading, where AI agents now research, back-test, and productionize trading signals. The core of their success lies in "Skills Governance"—treating AI skills as production-grade code with clear ownership, testing, and a centralized marketplace to ensure consistency and reliability across the organization.

## Key Points
- **AI in Systematic Trading:** AI agents handle the entire lifecycle of a trading signal: ideation, data retrieval, back-testing, proposal writing, and productionization.
- **The Iceberg Analogy:** The trading signal is just the tip; most of the value and complexity (data cleaning, outlier detection, infrastructure) lies in the workflows beneath it.
- **Skills as a Superpower:** Skills act as the connective layer between general-purpose models and proprietary institutional knowledge and data.
- **Governance Necessity:** Initial "local optimizations" by power users led to hardcoded errors and inconsistency; solved by creating a governed "marketplace" for skills.
- **Marketplace Model:** Skills are tagged, tested with evals, reviewed, and owned by the actual process owners (e.g., the Finance department owns finance skills).
- **Adoption and Scale:** Over 750 employees across all departments use Claude Code, supported by a library of 100+ governed skills.

## Notable Quotes
- "Organizational context... is your IP. It's your moat. It's one of the few safe spaces left in AI."
- "Treat those skills like production code because that's what they will become."
- "Adoption is not a licensing problem. It's a people problem."
- "Plan your approach before you plan the roll out."

## Takeaways
- Don't just augment existing workflows; rethink them for an agentic era to capture the full potential of AI.
- Establish a centralized, governed library for AI skills early to avoid fragmentation and ensure organizational consistency.
- Ensure skill ownership lies with the domain experts (process owners) to maintain accountability and quality.
