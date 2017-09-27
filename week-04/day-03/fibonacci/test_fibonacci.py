import unittest
import fibonacci


class FibonacciTest(unittest.TestCase):
    def test_index(self):
        self.assertEqual(fibonacci.fibonacci_counter(6), 8)


    def test_string_type(self):
        self.assertRaises(TypeError, fibonacci.fibonacci_counter("valami"))


    def test_boolean_type(self):
        self.assertRaises(TypeError, fibonacci.fibonacci_counter(False))


    def test_float_type(self):
        self.assertRaises(TypeError, fibonacci.fibonacci_counter(1.2))


    def test_insert_zero(self):
        self.assertEqual(fibonacci.fibonacci_counter(0), 0)


    def test_insert_null(self):
        self.assertEqual(fibonacci.fibonacci_counter(None), None)

if __name__ == "__main__":
    unittest.main()