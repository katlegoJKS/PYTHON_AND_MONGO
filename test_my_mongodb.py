import unittest

from my_mongodb import create_visitor
from my_mongodb import list_visitors
from my_mongodb import delete_visitor
from my_mongodb import update_visitor
from my_mongodb import visitor_details
from my_mongodb import delete_all

class TestMyMongdb(unittest.TestCase):

    def test_create_visitor(self):
        assert create_visitor

    def test_list_visitors(self):
        assert list_visitors

    def test_delete_visitor(self):
        assert delete_visitor

    def test_update_visitor(self):
        assert update_visitor

    def test_visitor_details(self):
        assert visitor_details

    def test_delete_all(self):
        assert delete_all