import  unittest

from tema2_nr_par import nr_par

class TestFunction(unittest.TestCase):
    def test_nr_par(self):
        self.assertTrue(nr_par(18))
        self.assertFalse(nr_par(19))

