import unittest
from gtr import GtR2Client

gtr = GtR2Client()

class TestGtR2Client(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(gtr.hello(), "world")

    def test_get_people(self):
        res = gtr.get_people({
            "page_size": 10
        })
        flag = isinstance(res, dict)
        self.assertEqual(flag, True)

    def test_get_projects(self):
        res = gtr.get_projects({
            "page_size": 10
        })
        flag = isinstance(res, dict)
        self.assertEqual(flag, True)