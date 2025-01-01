import unittest
from utils.validation_utils import is_valid_ip, is_valid_cidr

class TestValidation(unittest.TestCase):
    def test_is_valid_ip(self):
        self.assertTrue(is_valid_ip('192.168.1.1'))
        self.assertFalse(is_valid_ip('999.999.999.999'))

    def test_is_valid_cidr(self):
        self.assertTrue(is_valid_cidr('192.168.1.0/24'))
        self.assertFalse(is_valid_cidr('192.168.1.0/99'))

if __name__ == '__main__':
    unittest.main()