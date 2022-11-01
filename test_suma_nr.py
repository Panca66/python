
import unittest

from suma_nr import suma_nr

class TestFunction(unittest.TestCase):
    def test_suma_nr(self):
        self.assertEqual(suma_nr(2, 24), 26)
        self.assertEqual(suma_nr(35, 45), 80)
        
