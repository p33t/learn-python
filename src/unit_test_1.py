import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(22, 22)


if __name__ == '__main__':
    unittest.main()
