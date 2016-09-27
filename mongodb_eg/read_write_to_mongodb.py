from pymongo import MongoClient

# Set database name and collection
DB = "mydb1"
COLLECTION = "tutorialspoint1"

# Client to communicate with database
client = MongoClient()
# db refers to database
db = client[DB]


def write_to_db(data):
    """ Write document to collection in database"""
    try:
        result = db[COLLECTION].insert(data)
    except Exception as e:
        raise e

    return result


def read_from_db():
    """ Read document information from collection in database"""
    try:
        result = db[COLLECTION].find()
    except Exception as e:
        raise e
    
    return result


# Update method
# input : id, field 
def update_document(field, value, new_value):
    """ Update the content of document in collection """
    try:
        result = db[COLLECTION].update_one(
            {"%s"%(field) : "%s" %(value)}, 
            {
                "$set" : {"%s" %(field) : "%s" %(new_value)}
            })
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
    result = update_document("age", 28, 30)
    print "Documents in 'tutorialspoint' collection are :"
    documents = read_from_db()
    for document in documents:
        print "%s" %document
