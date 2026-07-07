#!/usr/bin/env python3
"""Quick test script for LM Studio + Qwen 2.5 integration.

Run this script to verify your LM Studio setup is working correctly.

Usage:
    python test_lmstudio.py

Make sure LM Studio is running with the Qwen model loaded first!
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Configuration
LM_STUDIO_BASE_URL = os.environ.get(
    "LM_STUDIO_BASE_URL", "http://localhost:1234/v1"
)
LM_STUDIO_MODEL = os.environ.get(
    "LM_STUDIO_MODEL", "qwen2.5-7b-instruct-q4_k_m"
)


def main() -> None:
    print(f"Connecting to LM Studio at: {LM_STUDIO_BASE_URL}")
    print(f"Using model: {LM_STUDIO_MODEL}")
    print("-" * 50)

    # Connect to LM Studio
    client = OpenAI(
        base_url=LM_STUDIO_BASE_URL,
        api_key="lm-studio",  # Placeholder, not validated
    )

    # Test the connection by listing models
    try:
        models = client.models.list()
        print("Available models:")
        for model in models.data:
            print(f"  - {model.id}")
        print("-" * 50)
    except Exception as e:
        print(f"Could not list models: {e}")

    # Chat with Qwen
    messages = [
        {
            "role": "system",
            "content": (
                "You are Qwen, a helpful AI assistant created by "
                "Alibaba Cloud. You are running locally via LM Studio."
            ),
        },
        {
            "role": "user",
            "content": (
                "Hello! Please introduce yourself briefly and "
                "confirm you're running locally."
            ),
        },
    ]

    print("Sending test message to Qwen...")
    print("-" * 50)

    try:
        response = client.chat.completions.create(
            model=LM_STUDIO_MODEL,
            messages=messages,
            temperature=0.7,
            max_tokens=512,
        )

        print("Response from Qwen:")
        print(response.choices[0].message.content)
        print("-" * 50)
        print("LM Studio integration is working!")

    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
        print("1. Is LM Studio running?")
        print("2. Is the Qwen model loaded?")
        print("3. Is the local server started in LM Studio?")
        print(f"4. Is the server running on {LM_STUDIO_BASE_URL}?")


if __name__ == "__main__":
    main()
