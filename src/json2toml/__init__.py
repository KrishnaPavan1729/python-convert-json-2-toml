"""
JSON to TOML Converter
Author: Your Name
GitHub: https://github.com/yourusername/json2toml

This is a personal project to demonstrate my Python programming skills,
particularly in the areas of file processing, data format conversion,
and software architecture.
"""

from .config import config
from .logging_setup import LoggerSetup, Logger
from .utils import TimeMeasurement, FileSizeCalculator, DynamicModel
from .converter import JSON2TOML

__all__ = [
    "config",
    "LoggerSetup",
    "Logger",
    "TimeMeasurement",
    "FileSizeCalculator",
    "DynamicModel",
    "JSON2TOML",
]

__version__ = "0.1.0"
