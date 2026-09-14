# Restack overview

Restack is a backend framework for building reliable AI agents and workflows.
Developers define workflows, agents, and functions in Python and register them
as a service that connects to the Restack engine.

Key concepts:

- Workflow: a durable, replayable orchestration of steps.
- Agent: a long-running entity that reacts to events (for example chat messages)
  and can call functions and child workflows.
- Function: a single unit of work (for example an LLM call or a database lookup).
- Engine: a local service (run via Docker) that schedules runs, stores run
  history, and exposes a Developer UI on port 5233 and an API on port 6233.

The engine persists the full event history of every run, which makes runs
replayable and debuggable from the Developer UI.
