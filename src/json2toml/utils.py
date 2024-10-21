import os
import time
from functools import wraps
from loguru import logger
from pydantic import BaseModel
from typing import Dict, Any

class TimeMeasurement:
    @staticmethod
    def timed(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed_time = time.perf_counter() - start_time
            logger.info(f"Function {func.__name__} executed in {elapsed_time:.3f} seconds")
            return result, elapsed_time
        return wrapper

class FileSizeCalculator:
    @staticmethod
    def get_file_size(filepath: str) -> float:
        return os.path.getsize(filepath)
    
    @staticmethod
    def log_filesize(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            instance = args[0]
            try:
                json_file_size = FileSizeCalculator.get_file_size(instance.json_file)
                logger.debug(f"Size of {instance.json_file}: {json_file_size} bytes")
                result = func(*args, **kwargs)
                if result[0]:
                    toml_file_size = FileSizeCalculator.get_file_size(instance.toml_file)
                    logger.debug(f"Size of {instance.toml_file}: {toml_file_size} bytes")
                return result
            except Exception as e:
                logger.error(f"Error in {func.__name__}: {e}")
                return False, 0.0
        return wrapper

class DynamicModel(BaseModel):
    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(**data)
