import logging
import os
from logging.handlers import TimedRotatingFileHandler


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
logger: logging.Logger = logging.getLogger("milenkobot")


def setup_logging():
    log_path = "./logs"
    os.makedirs(log_path, exist_ok=True)

    file_handler = TimedRotatingFileHandler(
        filename=f"{log_path}/bot.log",
        when="D",              # D = daily rotation
        backupCount=7,         # Guarda 7 días de logs
        encoding="utf-8"
    )
    file_handler.setFormatter(logging.Formatter(
        '{asctime} [{levelname:<8}] {name}: {message}',
        '%Y-%m-%d %H:%M:%S',
        style='{'
    ))

    console_handler = logging.StreamHandler()

    logging.basicConfig(
        level=logging.INFO,
        handlers=[file_handler, console_handler]
    )