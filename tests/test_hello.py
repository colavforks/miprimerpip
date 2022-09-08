import unittest
from desoper import miprimerpip


class Test_hello(unittest.TestCase):
    def test__working(self):
        self.assertEqual(miprimerpip.hello(),
                         'Hello, World!', True)


if __name__ == '__main__':
    unittest.main()
