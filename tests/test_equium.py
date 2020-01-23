from equium import Object
import unittest


class ObjectTest(unittest.TestCase):
    def test_same(self):
        obj = Object()
        self.assertFalse(obj == obj)


if __name__ == "__main__":
    unittest.main()
