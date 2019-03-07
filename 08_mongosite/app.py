from flask import Flask
import json, pymongo
app = Flask(__name__)

@app.route("/")
def main():

    SERVER_ADDR ="localhost"
    connection = pymongo.MongoClient(SERVER_ADDR)
    db = connection["cman"]
    collection = db.nobelprize
    
    print("liasdjfh")
    return "Hello"


if __name__=="__main__":
    app.debug = True
    #app.run()
    app.run(host = "0.0.0.0")
