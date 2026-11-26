from pathlib import Path

from logger import ConsoleStrategy, FileStrategy, UpperFileStrategy


def test_console_strategy_prints_message(capsys) -> None:
    ConsoleStrategy().write("hello")

    assert capsys.readouterr().out.strip() == "hello"


def test_file_strategy_appends_messages_and_creates_parent(tmp_path: Path) -> None:
    path = tmp_path / "nested" / "app.log"
    strategy = FileStrategy(path)

    strategy.write("first")
    strategy.write("second")

    assert path.read_text(encoding="utf-8") == "first\nsecond\n"


def test_upper_file_strategy_uppercases_message(tmp_path: Path) -> None:
    path = tmp_path / "app.log"

    UpperFileStrategy(path).write("hello World")

    assert path.read_text(encoding="utf-8") == "HELLO WORLD\n"
