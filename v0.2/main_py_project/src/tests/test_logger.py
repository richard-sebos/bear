import unittest
import os
from utils.logger import configure_logger

class TestLogger(unittest.TestCase):
    def test_logger_creation(self):
        logger = configure_logger()
        self.assertIsNotNone(logger)
        log_path = 'src/output/logs/app.log'
        self.assertTrue(os.path.exists(log_path))

if __name__ == '__main__':
    unittest.main()
