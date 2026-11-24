"""Week 1 smoke test: call Claude once and print the reply."""

import anthropic
from dotenv import load_dotenv

load_dotenv()  # reads ANTHROPIC_API_KEY from .env

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    output_config={"effort": "low"},
    betas=["server-side-fallback-2026-07-01"],
    fallbacks="default",
    messages=[
        {
            "role": "user",
            "content": "In one sentence, what is a Salesforce ops agent?",
        }
    ],
)

if response.stop_reason == "refusal":
    print("Request was declined:", response.stop_details)
else:
    print(next(b.text for b in response.content if b.type == "text"))
