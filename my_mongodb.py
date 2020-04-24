import pymongo

client = pymongo.MongoClient("mongodb://root:rootpass@localhost:27018/")
db = client["UmuziProspects"]
Visiter = db["Visiter"] 

def create_visitor(visitor):
    mydict = {
        'visiter_name': 'Jack',
        'visiters_age': '20',
        'date_of_vist': '01 January 2020',
        'time_of_visit': '13H00',
        'name_of_the_person_who_assisted_visiter': 'Daniels',
        'comments': 'Daniels was very much helpful'
    }
    result = Visiter.insert_one(mydict)
    return result

def list_visitors(visitors):
    for every_visitor in Visiter.find():
        print(every_visitor)

def delete_visitor(dltvisitor):
    myquery = { "visiter_name": "Jack"}
    Visiter.delete_one(myquery)

def update_visitor(upvisitor):
    query = { "visiter_name": "Kat" }
    newvalues = { "$set": { "visiters_age": "30" } }
    Visiter.update_one(query, newvalues)

def visitor_details(visitorinfo):
    myquery = { "visiter_name": "Kat" }
    mydoc = Visiter.find(myquery)
    return mydoc

def delete_all(deleteall):
    collection = Visiter.delete_many({})
    print(collection.deleted_count, "documents deleted")


# visitor = create_visitor('')
# print(visitor)

# visitors = list_visitors('')
# print(visitors)

# dltvisitor = delete_visitor('')

# upvisitor =update_visitor('')
# print(upvisitor)

# visitorinfo = visitor_details('')
# print(visitorinfo)

deleteall = delete_all('')

