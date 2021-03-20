import unittest
import codecs

from urllib.parse import urlparse, parse_qsl

class TestCase(unittest.TestCase):
    def assertURLEqual(self,first,second, msg=None):
        first_parsed = urlparse(first)
        second_parsed = urlparse(second)
        self.assertEqual(first_parsed[:3], second_parsed[:3], msg)

        first_qsl = sorted(parse_qsl(first_parsed.query))
        second_qsl = sorted(parse_qsl(second_parsed.query))
        self.assertEqual(first_qsl, second_qsl, msg)
