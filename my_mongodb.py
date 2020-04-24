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


visitors = list_visitors('')
print(visitors)