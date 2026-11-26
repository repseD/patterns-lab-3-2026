from pathlib import Path

from logger import (
    ConsoleLoggerCreator,
    ConsoleStrategy,
    FileLoggerCreator,
    FileStrategy,
    UpperFileLoggerCreator,
    UpperFileStrategy,
)


def test_console_creator_returns_console_strategy() -> None:
    assert isinstance(ConsoleLoggerCreator().create_strategy(), ConsoleStrategy)


def test_file_creator_returns_file_strategy(tmp_path: Path) -> None:
    path = tmp_path / "app.log"
    strategy = FileLoggerCreator(path).create_strategy()

    assert isinstance(strategy, FileStrategy)

    strategy.write("hello")
    assert path.read_text(encoding="utf-8") == "hello\n"


def test_upper_file_creator_returns_upper_file_strategy(tmp_path: Path) -> None:
    path = tmp_path / "app.log"
    strategy = UpperFileLoggerCreator(path).create_strategy()

    assert isinstance(strategy, UpperFileStrategy)

    strategy.write("hello")
    assert path.read_text(encoding="utf-8") == "HELLO\n"
