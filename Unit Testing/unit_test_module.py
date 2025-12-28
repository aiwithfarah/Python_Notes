import unittest

# --Your actual code--


def multiply(a, b):
    return a * b


# --Your Test Code--
class TestMath(unittest.TestCase):  # create the container

    def test_basic_multiplication(self):  # define a test scenario
        result = multiply(3, 4)
        self.assertEqual(result, 12)  # Check i it matches

    def test_multiply_by_zero(self):
        result = multiply(10, 0)
        self.assertEqual(result, 0)


# --Run the tests--
if __name__ == '__main__':
    unittest.main()

# ..     (2 dots means test has passed. If even one failed ypu would see an F with a detailed message)
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK
