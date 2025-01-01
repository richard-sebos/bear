import unittest
from utils.file_reader import read_file

class TestFileReader(unittest.TestCase):
    def test_read_file(self):
        with open('test_ips.txt', 'w') as file:
            file.write('192.168.1.1\n999.999.999.999\n')
        
        result = read_file('test_ips.txt')
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], '192.168.1.1')
        self.assertEqual(result[1], '999.999.999.999')

if __name__ == '__main__':
    unittest.main()