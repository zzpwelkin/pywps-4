import sys
import unittest

import parse
import extent

def load_tests():
    return unittest.TestSuite([parse.load_tests(), extent.load_tests()])

if __name__ == "__main__":
    result = unittest.TextTestRunner(verbosity=2).run(load_tests())
    if not result.wasSuccessful():
        sys.exit(1)
