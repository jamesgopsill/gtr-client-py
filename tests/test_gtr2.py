import unittest
from gtr import GtR2Client

gtr = GtR2Client()

class TestGtR2Client(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(gtr.hello(), "world")

    def test_people(self):
        res = gtr.people({
            "page_size": 10
        })
        flag = isinstance(res, dict)
        self.assertEqual(flag, True)

    def test_projects(self):
        res = gtr.projects({
            "page_size": 10
        })
        flag = isinstance(res, dict)
        self.assertEqual(flag, True)