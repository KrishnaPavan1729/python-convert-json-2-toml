from loguru import logger
from functools import wraps
from .config import config

class LoggerSetup:
    @staticmethod
    def setup_logger(logfile_path: str, logfile_name: str) -> None:
        log_level = "DEBUG" if config.debug_mode else "INFO"
        logger.remove()
        logger.add(f"{logfile_path}/{logfile_name}.log", 
                   format="{time:%Y-%m-%d %H:%M:%S.%f} | {level: <8} | {name}:{function}:{line} | {message}",
                   filter=lambda record: record["level"].name in ["INFO", "WARNING", "CRITICAL", "ERROR"] 
                                         or (config.debug_mode and record["level"].name == "DEBUG"),
                   level=log_level, rotation="10 MB", retention="1 week", compression="zip", 
                   serialize=True, enqueue=True)
        logger.add(lambda msg: print(msg, end=""), level=log_level, format="{message}")

class Logger:
    @staticmethod
    def log(level: str):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                if config.debug_mode or level.upper() != "DEBUG":
                    logger.log(level, f"Entering {func.__name__}")
                result = func(*args, **kwargs)
                if config.debug_mode or level.upper() != "DEBUG":
                    logger.log(level, f"Exiting {func.__name__}")
                return result
            return wrapper
        return decorator
