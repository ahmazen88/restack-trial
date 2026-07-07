import asyncio
import sys

from restack_ai import Restack


async def main(agent_id: str, run_id: str) -> None:
    client = Restack()

    # Send a message to the Qwen agent
    await client.send_agent_event(
        agent_id=agent_id,
        run_id=run_id,
        event_name="messages",
        event_input={
            "messages": [
                {
                    "role": "user",
                    "content": "Hello! Can you introduce yourself?",
                }
            ]
        },
    )

    # End the agent
    await client.send_agent_event(
        agent_id=agent_id,
        run_id=run_id,
        event_name="end",
        event_input={"end": True},
    )

    sys.exit(0)


def run_event_agent() -> None:
    # Update these with actual agent_id and run_id from schedule_agent
    asyncio.run(
        main(
            agent_id="<AGENT_ID>",
            run_id="<RUN_ID>",
        )
    )


if __name__ == "__main__":
    run_event_agent()
