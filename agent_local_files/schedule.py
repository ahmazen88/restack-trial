import asyncio
import sys
import time

from restack_ai import Restack

# Two natural turns: first retrieve from the local knowledge base, then save the
# result to a local file. Each turn is a single, reliable tool call.
TURN_1 = (
    "Using the local knowledge base, explain how this project runs agents fully "
    "offline and how the local knowledge base works."
)
TURN_2 = "Now save that explanation as a summary to 'summary.md'."


def _print_new(messages: list, seen: int) -> int:
    for message in messages[seen:]:
        role = message.get("role")
        content = message.get("content")
        if role == "tool":
            preview = (content or "").splitlines()[:1]
            print(f"[tool result] {preview[0] if preview else ''}")  # noqa: T201
        elif content:
            print(f"[{role}] {content}")  # noqa: T201
    return len(messages)


async def _ask(client: Restack, agent_id: str, run_id: str, text: str) -> list:
    return await client.send_agent_event(
        agent_id=agent_id,
        run_id=run_id,
        event_name="messages",
        event_input={"messages": [{"role": "user", "content": text}]},
        wait_for_completion=True,
    )


async def main() -> None:
    client = Restack()

    agent_id = f"{int(time.time() * 1000)}-AgentLocalFiles"
    run_id = await client.schedule_agent(
        agent_name="AgentLocalFiles", agent_id=agent_id
    )

    print("=== Conversation ===")  # noqa: T201
    seen = 0
    result = await _ask(client, agent_id, run_id, TURN_1)
    seen = _print_new(result, seen)
    result = await _ask(client, agent_id, run_id, TURN_2)
    seen = _print_new(result, seen)

    await client.send_agent_event(
        agent_id=agent_id, run_id=run_id, event_name="end"
    )

    sys.exit(0)


def run_schedule() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    run_schedule()
