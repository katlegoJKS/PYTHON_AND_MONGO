import unittest

from my_mongodb import create_visitor

class TestMyMongdb(unittest.TestCase):

    def test_create_visitor(self):
        assert create_visitor