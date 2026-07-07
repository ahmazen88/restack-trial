# LM Studio Agent - Qwen 2.5 7B Instruct

This agent integrates with [LM Studio](https://lmstudio.ai/) to run the Qwen 2.5 7B Instruct model (GGUF Q4_K_M quantization) locally via Python.

## Prerequisites

1. **LM Studio**: Download and install from https://lmstudio.ai/
2. **Qwen Model**: In LM Studio, download the model:
   - Search for: `Qwen2.5-7B-Instruct-GGUF`
   - Select the `Q4_K_M` quantization variant
   - Recommended file: `qwen2.5-7b-instruct-q4_k_m.gguf`

3. **Start LM Studio Server**:
   - Load the Qwen model in LM Studio
   - Go to "Local Server" tab
   - Click "Start Server"
   - Default endpoint: `http://localhost:1234/v1`

## Installation

```bash
cd agent_lm_studio
pip install restack-ai openai python-dotenv pydantic watchfiles
```

## Configuration

Create a `.env` file (optional):

```env
# LM Studio Configuration (defaults shown)
LM_STUDIO_BASE_URL=http://localhost:1234/v1
LM_STUDIO_MODEL=qwen2.5-7b-instruct-q4_k_m

# Restack Configuration (if using Restack Cloud)
RESTACK_ENGINE_ID=your_engine_id
RESTACK_ENGINE_ADDRESS=your_engine_address
RESTACK_ENGINE_API_KEY=your_api_key
RESTACK_ENGINE_API_ADDRESS=your_api_address
```

## Usage

### 1. Start the Services

```bash
cd agent_lm_studio
python -m src.services
```

### 2. Schedule an Agent

In a new terminal:

```bash
cd agent_lm_studio
python schedule_agent.py
```

### 3. Send Events to the Agent

Update `event_agent.py` with the `agent_id` and `run_id` from step 2, then:

```bash
python event_agent.py
```

## Standalone Usage (Without Restack)

You can also use the LM Studio integration directly without the Restack framework:

```python
from openai import OpenAI

# Connect to LM Studio
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"  # Placeholder, not validated
)

# Chat with Qwen
response = client.chat.completions.create(
    model="qwen2.5-7b-instruct-q4_k_m",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ],
    temperature=0.7,
    max_tokens=2048
)

print(response.choices[0].message.content)
```

## Model Information

- **Model**: Qwen 2.5 7B Instruct
- **Quantization**: Q4_K_M (4-bit quantization)
- **Format**: GGUF
- **RAM Usage**: ~5-6 GB
- **Context Length**: 32K tokens (default)

## API Reference

### LmStudioInput Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `messages` | `list[Message]` | `None` | Chat messages |
| `system_content` | `str` | `None` | System prompt |
| `model` | `str` | `qwen2.5-7b-instruct-q4_k_m` | Model identifier |
| `temperature` | `float` | `0.7` | Sampling temperature |
| `max_tokens` | `int` | `2048` | Max tokens to generate |

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `LM_STUDIO_BASE_URL` | `http://localhost:1234/v1` | LM Studio API endpoint |
| `LM_STUDIO_MODEL` | `qwen2.5-7b-instruct-q4_k_m` | Model to use |

## Troubleshooting

1. **Connection refused**: Ensure LM Studio server is running
2. **Model not found**: Check the model name matches what's loaded in LM Studio
3. **Slow responses**: Q4_K_M is optimized for speed/quality balance; consider Q8 for better quality or Q4_K_S for faster inference
