import unittest
from src import cicd
from nose2 import tools


class MyTestCase(unittest.TestCase):
    """
    def __init__(self):
        self.obj = cicd.cicd()
    """
    def setUp(self) -> None:
        self.obj= cicd.cicd()
    def test_something(self):
        #obj = cicd.cicd()
        ret =self.obj.process_count(1,2)
        self.assertEqual(ret,3)
    def test_multi(self):
        #obj = cicd.cicd()
        mult = self.obj.process_multi(1,2)
        self.assertEqual(mult,2,"multi")


if __name__ == '__main__':
    unittest.main()
