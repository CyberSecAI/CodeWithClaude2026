# How Lovable vibecodes production software at scale

## Executive Summary
Fabian Hedin (CTO, Lovable) discusses the mission to move AI-native development from "prototyping" to "production-grade" software. Lovable has reached massive scale, serving 600 million monthly sessions across 50 million projects. The session explores the "180% Rule" (where the last 10% of a project takes 90% of the time) and how Lovable uses fleet-learning, rigorous eval loops, and custom sandboxing to help non-technical users ship robust, bug-free applications using Claude.

## Key Points
- **Production-Grade Ambition:** Lovable isn't just for "vibecoding" prototypes; it's designed to ship complex, scalable web and mobile applications for everyone from children to Fortune 500 companies.
- **The "180% Rule":** AI makes the first 90% of a project instantaneous, but the remaining 10% (bugs, edge cases, production polish) is where the real engineering happens.
- **Infrastructure for Reliability:**
    - **Fleet-Learning Layer:** A system that analyzes coding mistakes across millions of projects and feeds those learnings back into the model's instructions to prevent recurrence.
    - **Rigorous Eval Loops:** Every model update is gated by a massive evaluation suite to ensure no regressions in code quality or architectural logic.
- **Scaling the "Unstackable":** Users are replacing fragmented stacks (Airtable + Zapier + Calendly) with single, integrated Lovable applications, significantly reducing complexity and cost.
- **The Interface:** A split-screen "Chat-and-Preview" UI that allows for real-time iteration and instant feedback.
- **The "Compactor" Tool:** An abstraction that helps users translate their web-based Lovable projects into mobile-ready applications.

## Notable Quotes
- "The first 90% of the code takes 90% of the time... and the remaining 10% takes the other 90%."
- "We're seeing 600 million monthly sessions on sites built with Lovable—more than our own traffic."
- "Our goal is to push the complexity, size, and ambition of what can be built with AI."

## Takeaways
- **Focus on the "Last 10%":** Use AI to handle the bulk of development, but dedicate your human "intent" to verification, edge cases, and production polish.
- **Implement a "Fleet-Learning" Feedback Loop:** If your team builds many projects, create a shared document (like `CLAUDE.md` or a "Skills" library) that logs common agent mistakes and their fixes.
- **Unify your Stack:** Look for opportunities to consolidate multiple SaaS tools into a single agent-built application to reduce "glue code" and architectural fragility.
- **Evaluate Every Shift:** Don't just "upgrade" to the newest model version without running a representative set of your own code tasks (evals) to ensure the agent hasn't lost its "edge" on your specific patterns.
