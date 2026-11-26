from .formatting import format_message
from .levels import LogLevel, parse_level
from .strategies import OutputStrategy


class Logger:
    def __init__(self, strategy: OutputStrategy) -> None:
        self._strategy = strategy

    def log(self, level: LogLevel | str, message: str) -> str:
        normalized = parse_level(level)
        formatted = format_message(normalized, message)
        self._strategy.write(formatted)
        return formatted
