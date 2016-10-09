#!flask/bin/python
from flask import Flask
import pymongo
from flask_cors import CORS, cross_origin
from bson.json_util import dumps

app = Flask(__name__)
CORS(app)

client = pymongo.MongoClient()
db = client.test

@app.route('/', methods=['GET'])
def get_tasks():
	task = db['test_form'].find_one()
	return dumps(task) 

if __name__ == '__main__':
    app.run(debug=True)