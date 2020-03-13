import unittest
from src import cicd


class MyTestCase(unittest.TestCase):
    """
    def __init__(self):
        self.obj = cicd.cicd()
    """

    def test_something(self):
        obj = cicd.cicd()
        ret =obj.process_count(1,2)
        self.assertEqual(ret,3)
    def test_multi(self):
        obj = cicd.cicd()
        mult = obj.process_multi(1,2)
        self.assertEqual(mult,1,"multi")


if __name__ == '__main__':
    unittest.main()
