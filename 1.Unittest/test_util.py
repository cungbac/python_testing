import unittest

from util import trim_account_number
from Mocks.Current.main import add

class TestUtil(unittest.TestCase):
    def test_trim_account_number(self):
        self.assertEqual(trim_account_number('1234567890'), '2345678900')

if __name__ == '__main__':
    unittest.main()