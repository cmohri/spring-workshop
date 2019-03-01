#Amit Narang and Clara Mohri
#CMAN
#SoftDev pd06
#K06 -- Yummy Mongo Py
#2019-02-28

import pymongo

SERVER_ADDR = "167.99.1.24"
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection.test
collection = db['primer-dataset']

def findBorough(borough):
    return collection.find({"borough":borough})

def findZip(zip):
    return collection.find({"address.zipcode":zip})

def findZipGrade(zip,grade):
    return collection.find({$and: [{"address.zipcode":zip},{"grade.0.grade":grade}]})

def findZipScore(zip,score):
    return collection.find({$and: [{"address.zipcode":zip},{"grade.0.score":score}]})

