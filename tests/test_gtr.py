import unittest
from gtr import GtRClient

class TestGtRClient(unittest.TestCase):
    def test_hello(self):
        gtr = GtRClient()
        self.assertEqual(gtr.hello(), "world")