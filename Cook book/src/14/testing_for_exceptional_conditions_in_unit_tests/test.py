import unittest


# A simple function to illustrate
def parse_int(s):
    return int(s)


class TestConversion(unittest.TestCase):
    # Testing that an exception gets raised
    def test_bad_int(self):
        self.assertRaises(ValueError, parse_int, "N/A")

    # Testing an exception plus regex on exception message
    def test_bad_int_msg(self):
        self.assertRaisesRegex(ValueError, 'invalid literal .*', parse_int, 'N/A')

    # Example of testing an exception along with inspection of exception instance


import errno


class TestIO(unittest.TestCase):
    def test_file_not_found(self):
        try:
            f = open('/file/not/found')
        except IOError as e:
            self.assertEqual(e.errno, errno.ENOENT)
        else:
            self.fail("IOError not raised")


if __name__ == '__main__':
    unittest.main()
