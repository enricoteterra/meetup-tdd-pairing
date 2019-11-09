import unittest

# to run tests, use: `python -m unittest discover`


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(1+1, 3)


if __name__ == '__main__':
    unittest.main()
