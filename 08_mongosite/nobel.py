# CMAN
# Clara Mohri, Amit Narang
# SoftDev2 Pd6
# K06 -- Import/Export Bank
# 2019-03-05

'''
The name of the dataset we used is Nobel Prize winners. 
Hyperlink: http://api.nobelprize.org/v1/prize.json
In order to import, first downloaded the dataset. We connected to Mongo on the localhost server and created the cman database with this Python file. In Terminal, we used mongoimport --file nobelprize.json

This dataset contains information about all of the Nobel prize winners, like which category the prize was given in, which year, how many recipients there were, and what the motivation for their work was.. 
'''

import json
import pymongo

SERVER_ADDR = "localhost"
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection["cman"]
collection = db.nobelprize

db.collection.drop()
with open("nobelprize.json") as f:
    file_data = json.load(f)

# only run this once. Then comment:
#collection.insert(file_data["prizes"])

# get motivation by year
def year(year):
    print("In year: " + year )
    for i in (collection.find({"year":year})):
        print("Motivation: " + i["laureates"][0]["motivation"][1:-1] + "\n")

# get year and category for surname
def surname(surname):
    print("Nobel prizes awarded to last name: " + surname)
    for i in collection.find({"laureates.surname": surname}):
        print("year: " + i["year"])
        print("category: " + i["category"])

# nobel prizes by number of people awarded
def num_winners(num):
    print("Categories and years for which the number of people awarded was: " + num)
    for i in collection.find({"laureates.share": num}):
        print("year: " + i["year"])
        print("category: " + i["category"])

# nobel prizes by first name
def first_name(firstname):
    print("Nobel prizes awarded to people with the first name: " + firstname)
    for i in collection.find({"laureates.firstname": firstname}):
        surname = i["laureates"][0]["surname"]
        f = i["laureates"][0]["firstname"]
        year = (i["year"])
        print(f + " " + surname + " in " + year)

year("2017")
print("=======================================================")
surname("Henderson")
print("=======================================================")
num_winners("4")
print("=======================================================")
first_name("Denis")
