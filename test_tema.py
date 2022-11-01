
import unittest

from tema_teste import double_val


class TestFunction(unittest.TestCase):
    def test_double_val(self):
        self.assertEqual(double_val(8), 16)
        self.assertEqual(double_val(17), 34)
