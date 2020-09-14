import unittest
import katas
import random

x = random.randrange(1, 50, 3)
y = random.randrange(1, 50, 3)
n = random.randrange(1, 50, 3)

add_answer = x + y
multiply_answer = x * y
power_answer = x**n


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(x, y), add_answer)

    def test_multiply(self):
        self.assertEqual(katas.multiply(x, y), multiply_answer)

    def test_power(self):
        self.assertEqual(power(x, n), power_answer)

    def test_factorial(self):
        fact_answer = katas.factorial(5)
        self.fail(fact_answer, 120)

    def test_fibonacci(self):
        fib_answer = katas.fibonacci(50)
        self.fail(fib_answer, 12586269025)


if __name__ == '__main__':
    unittest.main()
