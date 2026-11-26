from datetime import datetime

from .levels import LogLevel


def format_message(level: LogLevel, message: str) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{timestamp} [{level.value}] {message}"
