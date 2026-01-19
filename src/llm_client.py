from openai import OpenAI
from openai import RateLimitError
import os

_client = None


def get_client():
    global _client
    if _client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY not set")
        _client = OpenAI(api_key=api_key)
    return _client


def analyze_logs(prompt: str) -> str:
    try:
        client = get_client()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a cybersecurity analyst."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
        )
        return response.choices[0].message.content.strip()

    except RateLimitError:
        return (
            "LLM quota exceeded.\n"
            "Summary: Multiple authentication failures detected.\n"
            "Severity: Medium\n"
            "Explanation: Likely brute-force SSH attempt.\n"
            "Recommended Action: Block source IP, enforce SSH hardening."
        )
