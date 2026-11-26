from abc import ABC, abstractmethod
from pathlib import Path

from .strategies import (
    ConsoleStrategy,
    FileStrategy,
    OutputStrategy,
    UpperFileStrategy,
)


class LoggerCreator(ABC):
    @abstractmethod
    def create_strategy(self) -> OutputStrategy:
        raise NotImplementedError


class ConsoleLoggerCreator(LoggerCreator):
    def create_strategy(self) -> OutputStrategy:
        return ConsoleStrategy()


class FileLoggerCreator(LoggerCreator):
    def __init__(self, path: str | Path = "application.log") -> None:
        self._path = path

    def create_strategy(self) -> OutputStrategy:
        return FileStrategy(self._path)


class UpperFileLoggerCreator(LoggerCreator):
    def __init__(self, path: str | Path = "application.log") -> None:
        self._path = path

    def create_strategy(self) -> OutputStrategy:
        return UpperFileStrategy(self._path)
