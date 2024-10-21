import ujson
import tomlkit
import chardet
from typing import Tuple, Dict, Any
from loguru import logger
from pydantic import ValidationError
from .logging_setup import Logger
from .utils import TimeMeasurement, FileSizeCalculator, DynamicModel

class JSON2TOML:
    def __init__(self, json_file: str, toml_file: str):
        self.json_file = json_file
        self.toml_file = toml_file
    
    @staticmethod
    def _get_exception_message(e: Exception) -> str:
        return f"{type(e).__name__}: {e}"
    
    def validate_json(self, json_data: Dict[str, Any]) -> bool:
        try:
            DynamicModel.from_dict(json_data)
            return True
        except ValidationError as e:
            logger.error(f"JSON validation Failed: {e}")
            return False
    
    def validate_toml(self, toml_data: Dict[str, Any]) -> bool:
        try:
            DynamicModel.from_dict(toml_data)
            return True
        except ValidationError as e:
            logger.error(f"TOML validation Failed: {e}")
            return False
    
    @Logger.log("INFO")
    @TimeMeasurement.timed
    @FileSizeCalculator.log_filesize
    def convert_json2toml(self) -> Tuple[bool, float]:
        try:
            with open(self.json_file, 'rb') as jsonfile:
                raw_data = jsonfile.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']
            with open(self.json_file, 'r', encoding=encoding) as jsonfile:
                json_data = ujson.load(jsonfile)
            if not self.validate_json(json_data):
                logger.error("Invalid JSON file. Conversion aborted")
                return False, 0.0
            toml_data = tomlkit.dumps(json_data)
            with open(self.toml_file, 'w', encoding=encoding, buffering=8192) as tomlfile:
                tomlfile.write(toml_data)
            if not self.validate_toml(tomlkit.parse(toml_data)):
                logger.error("Invalid TOML output. Conversion Failed.")
                return False, 0.0
            return True, 0.0
        except Exception as e:
            logger.error(f"Failed due to Exception: {self._get_exception_message(e)}")
            return False, 0.0
