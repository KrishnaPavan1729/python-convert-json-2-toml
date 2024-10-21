import os
import unittest
from src.json2toml.converter import JSON2TOML
from src.json2toml.config import config
from src.json2toml.logging_setup import LoggerSetup

class TestJSONToTOML(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        LoggerSetup.setup_logger('logs', 'test')

    def test_convert_valid_json(self):
        json2toml = JSON2TOML('tests/data/valid.json', 'tests/data/output.toml')
        success, _ = json2toml.convert_json2toml()
        self.assertTrue(success)
        self.assertTrue(os.path.exists('tests/data/output.toml'))

    def test_convert_invalid_json(self):
        json2toml = JSON2TOML('tests/data/invalid.json', 'tests/data/output.toml')
        success, _ = json2toml.convert_json2toml()
        self.assertFalse(success)

    def test_file_size_calculation(self):
        json2toml = JSON2TOML('tests/data/valid.json', 'tests/data/output.toml')
        _, _ = json2toml.convert_json2toml()
        self.assertGreater(config.get_file_size('tests/data/output.toml'), 0)

if __name__ == '__main__':
    unittest.main()
