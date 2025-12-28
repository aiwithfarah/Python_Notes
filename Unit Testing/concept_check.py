import unittest


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


class TextEvenNumber(unittest.TestCase):

    def test_even_number(self):
        result = is_even(4)
        self.assertEqual(result, True)

    def test_odd_number(self):
        result = is_even(5)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
