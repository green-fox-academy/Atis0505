import unittest
import demo


class DemoTest(unittest.TestCase):
    def test_add_def(self):
        self.assertEqual(demo.add(2,3), 5)

    
    def test_subst_def(self):
        self.assertEqual(demo.subst(2,5), -3)

    
    def test_multiple(self):
        self.assertEqual(demo.multiple(2,5), 10)


    def test_multiple(self):
        self.assertEqual(demo.multiple(2,-5), -10)

    
    def test_divide(self):
        self.assertEqual(demo.divide(9,3), 3)

    
    def test_divi(self):
        self.assertEqual(demo.divide(0,3), 0)

    
    def test_divide(self):
        self.assertEqual(demo.divi(3,0), 0)


if __name__ == "__main__":
    unittest.main()
    