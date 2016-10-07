#!flask/bin/python
from flask import Flask
import pymongo
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

client = pymongo.MongoClient()
db = client.test


@app.route('/', methods=['GET'])
def get_tasks():
	task = db.test_form.find_one()
	return task

if __name__ == '__main__':
    app.run(debug=True)