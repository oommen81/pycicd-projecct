import unittest
from src import cicd



class MyTestCase(unittest.TestCase):
    """
    def __init__(self):
        self.obj = cicd.cicd()
    """
    def setUp(self) -> None:
        self.obj= cicd.cicd()
    def test_something(self):
        #obj = cicd.cicd()
        print("test1")
        ret =self.obj.process_count(1,2)
        self.assertEqual(ret,3)
    def test_multi(self):
        #obj = cicd.cicd()
        mult = self.obj.process_multi(1,2)
        self.assertEqual(mult,2,"multi")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    testfunctions = ['test_something']
    for fns in testfunctions :
        suite.addTest(MyTestCase(fns))    #unittest.main()
    unittest.TextTestRunner(verbosity=2).run(suite)

