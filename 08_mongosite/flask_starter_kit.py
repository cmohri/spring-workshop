# Team Forest- Maggie Zhao, Kaitlin Wan, Clara Mohri
# SoftDev1 pd6
# K08 -- Ay Mon, Go Git It From Yer Flask
# 2019-03-07


from flask import Flask,render_template, request, session, url_for, redirect, flash
import pymongo
import pprint
import json
import os
app = Flask(__name__) #create instance of class flask

app.secret_key = os.urandom(32)

'''
Nobel Prize Database
Contains information about Nobel Prize winners like their name, birthdate, birth country, the prizes they won, what year they won it, the category of their work, and the reason for winning the prize.
Raw Data: http://api.nobelprize.org/v1/prize.json
Import Directions:
    mongoimport --db <DATABASE_NAME> --collection <COLLECTION_NAME> --drop --file PATH/prizes.json
'''

SERVER_ADDR = "localhost"
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection["Forest"]
collection = db.nobel



db.collection.drop()
with open("prizes.json") as f:
    file_data = json.load(f)

collection.insert(file_data["prizes"])

@app.route("/", methods = ["GET", "POST"])
def main():
    # try for wrong ip
    # try for no server open
    SERVER_ADDR = "localhost"
    #try:
    if request.method == "GET":
        return render_template('index.html', server = SERVER_ADDR )
    else:
        server = request.form['ip']
        if ( server ):
            SERVER_ADDR = server
            connection = pymongo.MongoClient(SERVER_ADDR)
            db = connection["Forest"]
            collection = db.laureates

            db.collection.drop()
            with open("prizes.json") as f:
                file_data = json.load(f)
            collection.insert(file_data["prize"])
        return render_template(redirect(url_for('search')))

    #except:
    #    return redirect('/')

@app.route("/search", methods = ["GET", "POST"])
def search():

    #try:
    if request.method == "GET":
        return render_template('base.html')
    else:
        type = request.form['option']
        input = request.form['input']
        print(type)
        print(input)
        if type == 'surname':
            result = surname(input)
        if type == 'year':
            result = year(input)
        if type == 'name':
            result = first_name(input)
        if type == 'num':
            result = num_winners(input)
        return render_template('base.html', results = result)

    #except:
    #    return redirect('/search')

# get motivation by year
def year(year):
    s = "In year: " + year + "<br>"
    for i in (collection.find({"year":year})):
        s += "Motivation: " + i["laureates"][0]["motivation"][1:-1] + "<br>"
    return s

# get year and category for surname
def surname(surname):
    s = "Nobel prizes awarded to last name: " + surname + "<br>"
    for i in collection.find({"laureates.surname": surname}):
        s += "year: " + i["year"] + "<br>"
        s += "category: " + i["category"] + "<br>"
    return s

# nobel prizes by number of people awarded
def num_winners(num):
    s = "Categories and years for which the number of people awarded was: " + num + "<br>"
    for i in collection.find({"laureates.share": num}):
        s += "year: " + i["year"] + "<br>"
        s += "category: " + i["category"] + "<br>"
    return s

# nobel prizes by first name
def first_name(firstname):
    s = "Nobel prizes awarded to people with the first name: " + firstname + "<br>"
    for i in collection.find({"laureates.firstname": firstname}):
        surname = i["laureates"][0]["surname"]
        f = i["laureates"][0]["firstname"]
        year = (i["year"])
        s += f + " " + surname + " in " + year + "<br>"
    return s



if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0")
