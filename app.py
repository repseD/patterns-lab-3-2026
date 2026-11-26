from logger import (
    ConsoleLoggerCreator,
    FileLoggerCreator,
    Logger,
    LogLevel,
    UpperFileLoggerCreator,
)

LOG_FILE = "logs/app.log"


def main() -> None:
    console_logger = Logger(ConsoleLoggerCreator().create_strategy())
    file_logger = Logger(FileLoggerCreator(LOG_FILE).create_strategy())
    upper_file_logger = Logger(UpperFileLoggerCreator(LOG_FILE).create_strategy())

    console_logger.log(LogLevel.INFO, "Application started")
    file_logger.log(LogLevel.WARN, "Low disk space")
    upper_file_logger.log(LogLevel.ERROR, "Example error")


if __name__ == "__main__":
    main()
