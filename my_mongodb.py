import pymongo
import os

HOST = os.environ.get('MONGO_DB')

client = pymongo.MongoClient(HOST)
db = client["UmuziProspects"]

Visitor = db["Visitor"] 

def create_visitor(visitor):
    Visitor.insert_one(visitor)
    return "visitor successfully created"

def list_visitors(visitors):
    for every_visitor in Visitor.find():
        print(every_visitor)

def delete_visitor(delete_a_visitor):
    Visitor.delete_one(delete_a_visitor)
    return "successfully deleted a visitor"

def update_visitor(visitor_to_update, visitors_new_age):
    Visitor.update_one(visitor_to_update, visitors_new_age)
    return "successfully updated visitor"

def visitor_details(visitor_info):
    documentary = Visitor.find(visitor_info)
    return documentary

def delete_all(delete_all_enteries):
    Visitor.delete_many({})
    return "documents deleted"


# visitor = create_visitor(
#     {'visitor_name': 'Junkis malwela',
#     'visitors_age': '28',
#     'date_of_vist': '01 Apr 2020',
#     'time_of_visit': '115H00',
#     'name_of_the_person_who_assisted_visitor': 'Daniels',
#     'comments': 'Shap yena he was very much helpful shem'}
#     )

# visitors = list_visitors('')

# delete_a_visitor = delete_visitor(
#     {'visitor_name': "Jack"}
#     )

# visitor_to_update =update_visitor(
#     {'visitor_name': "Junkis malwela"}, {'$set': { 'visitors_age': "55" }}
#     )

# visitor_info = visitor_details(
#     { "visitor_name": "Kat" }
#     )

# delete_all_enteries = delete_all('')