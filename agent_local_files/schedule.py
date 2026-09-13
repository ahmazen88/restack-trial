import asyncio
import sys
import time

from restack_ai import Restack

# The question the agent will answer using only local files + local models.
QUESTION = (
    "Using the local knowledge base, explain how this project runs agents "
    "fully offline and how the local knowledge base works. Then write a short "
    "summary to 'summary.md' and tell me where you saved it."
)


async def main() -> None:
    client = Restack()

    agent_id = f"{int(time.time() * 1000)}-AgentLocalFiles"
    run_id = await client.schedule_agent(
        agent_name="AgentLocalFiles", agent_id=agent_id
    )

    result = await client.send_agent_event(
        agent_id=agent_id,
        run_id=run_id,
        event_name="messages",
        event_input={"messages": [{"role": "user", "content": QUESTION}]},
        wait_for_completion=True,
    )

    print("=== Conversation ===")  # noqa: T201
    for message in result:
        role = message.get("role")
        content = message.get("content")
        if role == "tool":
            preview = (content or "").splitlines()[:1]
            print(f"[tool result] {preview[0] if preview else ''}")  # noqa: T201
        elif content:
            print(f"[{role}] {content}")  # noqa: T201

    await client.send_agent_event(
        agent_id=agent_id, run_id=run_id, event_name="end"
    )

    sys.exit(0)


def run_schedule() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    run_schedule()
