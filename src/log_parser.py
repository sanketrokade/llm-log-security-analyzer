
"""
log_parser.py

Responsibilities:
- Read log files
- Clean and normalize log lines
- Filter potentially important security/system events
- Chunk logs for LLM-safe processing
"""

from typing import List


KEYWORDS = [
    "error",
    "failed",
    "unauthorized",
    "denied",
    "invalid",
    "attack",
    "alert",
    "critical",
]


def read_log_file(file_path: str) -> List[str]:
    """
    Reads a log file and returns non-empty lines.
    """
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    return [line.strip() for line in lines if line.strip()]


def filter_important_lines(lines: List[str]) -> List[str]:
    """
    Filters lines that may indicate security or system issues.
    """
    important = []
    for line in lines:
        lower = line.lower()
        if any(keyword in lower for keyword in KEYWORDS):
            important.append(line)

    return important


def chunk_lines(lines: List[str], max_lines: int = 20) -> List[List[str]]:
    """
    Splits log lines into chunks to avoid overloading LLM context.
    """
    chunks = []
    for i in range(0, len(lines), max_lines):
        chunks.append(lines[i : i + max_lines])
    return chunks
