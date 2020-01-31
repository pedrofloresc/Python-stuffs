from main import fortest
import unittest


class ddddd(unittest.TestCase):
    def test(self):
        self.assertEqual(fortest(), 1, "LOL")

    def test2(self):
        self.assertFalse(False, "is false!")


if __name__ == "__main__":
    unittest.main()
