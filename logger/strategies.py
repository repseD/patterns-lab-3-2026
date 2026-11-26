from abc import ABC, abstractmethod
from pathlib import Path


class OutputStrategy(ABC):
    @abstractmethod
    def write(self, message: str) -> None:
        raise NotImplementedError


class ConsoleStrategy(OutputStrategy):
    def write(self, message: str) -> None:
        print(message)


class FileStrategy(OutputStrategy):
    def __init__(self, path: str | Path = "application.log") -> None:
        self._path = Path(path)

    def write(self, message: str) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        with self._path.open("a", encoding="utf-8") as stream:
            stream.write(message + "\n")


class UpperFileStrategy(FileStrategy):
    def write(self, message: str) -> None:
        super().write(message.upper())
