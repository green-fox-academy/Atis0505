import unittest
from Sharpie import Sharpie

sharpie = Sharpie("red", 12.2, 10)

class SharpieTest(unittest.TestCase):
    def test_sharpie_use(self):
        self.assertEqual(sharpie.use(), 9)


    def test_
if __name__ == "__main__":
    unittest.main()