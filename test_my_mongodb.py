import unittest

from my_mongodb import create_visitor
from my_mongodb import list_visitors
from my_mongodb import delete_visitor
from my_mongodb import update_visitor
from my_mongodb import visitor_details
from my_mongodb import delete_all

class TestMyMongdb(unittest.TestCase):

    def test_create_visitor(self):
        create_a_visitor = Visitor.insert_one(visitor)
        assert create_a_visitor.create_visitor() == "visitor successfullly created"

    def test_unsuccessful_create_visitor(self):
        create_a_visitor = Visitor.insert_one()
        assert create_a_visitor.create_visitor() == "visitor not created"

    def test_delete_visitor(self):
        delete_a_visitor = Visitor.delete_one(delete_a_visitor)
        assert delete_a_visitor.delete_visitor() == "visitor deleted"

    def test_update_visitor(self):
        update_a_visitor = Visitor.update_one(visitor_to_update, visitors_new_age)
        assert update_a_visitor.update_visitor() == "successfully updated visitor"

    def test_visitor_not_updated(self):
        update_a_visitor = Visitor.update_one()
        assert update_a_visitor.update_visitor() == "visitor not updated"

    def test_visitor_details(self):
        visitor_information = Visitor.find(visitor_info)
        assert visitor_information.visitor_details()

    def test_delete_all(self):
        delete_all_documents = Visitor.delete_many({})
        assert delete_all_documents.delete_all() == "documents deleted"

if __name__ == '__main__':
    unittest.main()