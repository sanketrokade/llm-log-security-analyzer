"""
analyzer.py

Main entry point for LLM-based log analysis.
"""

import sys
from pathlib import Path

from log_parser import read_log_file, filter_important_lines, chunk_lines
from llm_client import analyze_logs


PROMPT_FILE = Path("prompts/log_analysis_prompt.txt")


def load_prompt_template() -> str:
    return PROMPT_FILE.read_text(encoding="utf-8")


def build_prompt(template: str, log_chunk: list[str]) -> str:
    logs_text = "\n".join(log_chunk)
    return f"{template}\n\nLog Entries:\n{logs_text}"


def main():
    if len(sys.argv) < 2:
        print("Usage: python src/analyzer.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]

    lines = read_log_file(log_file)
    important = filter_important_lines(lines)

    if not important:
        print("No important log entries found.")
        return

    chunks = chunk_lines(important)
    template = load_prompt_template()

    for idx, chunk in enumerate(chunks, 1):
        print(f"\n=== Analysis for Chunk {idx} ===\n")
        prompt = build_prompt(template, chunk)
        result = analyze_logs(prompt)
        print(result)


if __name__ == "__main__":
    main()
