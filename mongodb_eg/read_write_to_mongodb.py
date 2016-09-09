from pymongo import MongoClient

# Client to communicate with database
client = MongoClient()
# db refers to 'mydb' database
db = client.mydb


def write_to_db(data):
    """ Write document to collection in database"""
    try:
        result = db.tutorialspoint.insert(data)
    except Exception as e:
        raise e

    return result


def read_from_db():
    """ Read document information from collection in database"""
    try:
        result = db.tutorialspoint.find()
    except Exception as e:
        raise e
    
    return result

if __name__ == "__main__":
    data = { "name": "Paras",
        "surname" : "Rajput",
        "location" : "Pune",
        "age" : "28"}
    result = write_to_db(data)
    print "Sucessfully inserted document with Object ID : %s" %result
    print "Documents in 'tutorialspoint' collection are :"
    documents = read_from_db()
    for document in documents:
        print "%s" %document
