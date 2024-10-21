import configparser
from typing import Any

class Config:
    def __init__(self, config_file='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
    
    def get(self, section: str, key: str, fallback: Any = None) -> Any:
        return self.config.get(section, key, fallback=fallback)
    
    @property
    def debug_mode(self) -> bool:
        return self.config.getboolean('Logging', 'debug_mode', fallback=False)

config = Config()
