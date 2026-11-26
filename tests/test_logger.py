import re

import pytest

from logger import Logger, LogLevel, OutputStrategy, format_message


class RecordingStrategy(OutputStrategy):
    def __init__(self) -> None:
        self.messages: list[str] = []

    def write(self, message: str) -> None:
        self.messages.append(message)


def test_format_message_has_required_format() -> None:
    formatted = format_message(LogLevel.INFO, "hello")

    assert re.fullmatch(
        r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[INFO\] hello",
        formatted,
    )


def test_logger_writes_formatted_message() -> None:
    strategy = RecordingStrategy()
    logger = Logger(strategy)

    result = logger.log(LogLevel.ERROR, "boom")

    assert result in strategy.messages
    assert "[ERROR] boom" in result


def test_logger_accepts_lowercase_level() -> None:
    strategy = RecordingStrategy()
    logger = Logger(strategy)

    result = logger.log("warn", "careful")

    assert "[WARN] careful" in result


def test_logger_rejects_unknown_level() -> None:
    strategy = RecordingStrategy()
    logger = Logger(strategy)

    with pytest.raises(ValueError, match="Unknown log level: DEBUG"):
        logger.log("DEBUG", "hello")

    assert strategy.messages == []
