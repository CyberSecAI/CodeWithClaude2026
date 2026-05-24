# Designing with Claude: From prompt to production

## Executive Summary
Dan Carey (Product Lead, Anthropic Labs) discusses the "Speed Gap" in modern software development. While engineering execution has been compressed from weeks to hours by tools like Claude Code, the "upstream" processes of product design and requirements gathering remain slow. The session introduces **Claude Design**—a toolset that allows for high-fidelity prototyping from raw context (meeting transcripts, rough notes) and provides a direct API bridge to production code.

## Key Points
- **The "Speed Gap":** Engineering is fast; Product and Design are still using slow cycles (PRDs, static mockups). This creates a new bottleneck.
- **Skip the PRD:** Documents are abstract and lead to team "hallucinations." A prototype is a "concrete thinking interface" that aligns the team faster.
- **Context-First Design:**
    - Feed Claude raw context: User interview transcripts, brand color JSONs, current UI screenshots.
    - Ask for three distinct prototype directions based on one "seed" (e.g., a meeting transcript).
- **Snapshotting:** Use Claude Design to create a "snapshot" of your design system, ensuring all generated prototypes adhere to brand guidelines.
- **Iterative Feedback (Edit vs. Comment):**
    - **Edit Mode:** For surgical tweaks to text or styles without re-generating the whole view.
    - **Comment Mode:** For contextual feedback that the agent uses to refine the next version.
- **The Production Bridge:** The **"Hand-off to Claude Code" API** allows engineers to pull a validated prototype directly into their IDE as functional code, bridging the gap between design and implementation.
- **Labs Engineering Culture:** "Build your own tools." If a task (like feedback analysis) is a papercut, spend an afternoon building a custom internal tool for it.

## Notable Quotes
- "A prototype is a concrete thinking interface for the team. Documents are abstract; prototypes are real."
- "The bottleneck is no longer how fast we can code; it's how fast we can decide what to build."
- "Build at the edge—build features the model *almost* handles well, because the next update will make them ship-ready."

## Takeaways
- **Replace your next PRD with a Prototype:** Feed your brainstorm notes into Claude Design and iterate on a live UI instead of a text doc.
- **Snapshot your Design System:** Upload your Tailwind configs and brand assets to Claude to ensure agent-generated UI is production-consistent.
- **Embrace the "24-Hour Fix":** Use the Design-to-Code workflow to take a user report and ship a visible UI fix within one day.
- **Build Internal "Papercut" Tools:** Don't wait for a formal roadmap; empower individual engineers to build the small agentic tools they need to be productive.
