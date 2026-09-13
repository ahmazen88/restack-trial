import asyncio
import sys
import time

from restack_ai import Restack


async def main() -> None:
    client = Restack()

    agent_id = f"{int(time.time() * 1000)}-AgentOllama"
    run_id = await client.schedule_agent(
        agent_name="AgentOllama", agent_id=agent_id
    )

    # Send a user message; the "messages" event handler returns the full
    # conversation, so we can print the assistant's reply.
    result = await client.send_agent_event(
        agent_id=agent_id,
        run_id=run_id,
        event_name="messages",
        event_input={
            "messages": [
                {
                    "role": "user",
                    "content": "What apparel is currently on sale?",
                }
            ]
        },
        wait_for_completion=True,
    )

    print("=== Conversation ===")  # noqa: T201
    for message in result:
        role = message.get("role")
        content = message.get("content")
        if content:
            print(f"[{role}] {content}")  # noqa: T201

    # Stop the agent run.
    await client.send_agent_event(
        agent_id=agent_id,
        run_id=run_id,
        event_name="end",
    )

    sys.exit(0)


def run_schedule() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    run_schedule()
