from enum import Enum


class LogLevel(str, Enum):
    TRACE = "TRACE"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"


def parse_level(level: LogLevel | str) -> LogLevel:
    if isinstance(level, LogLevel):
        return level
    try:
        return LogLevel(level.upper())
    except (AttributeError, ValueError) as error:
        raise ValueError(f"Unknown log level: {level}") from error
