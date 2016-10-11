#!flask/bin/python
from flask import Flask, request
import pymongo
from flask_cors import CORS, cross_origin
from bson.json_util import dumps

app = Flask(__name__)
CORS(app)

client = pymongo.MongoClient()
db = client.test

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
	if request.method == 'POST':
		if request.headers['Content-Type'] == 'application/json':
			task = request.get_json()
			db.test_form.insert_one(task)
			return 'Posted' 

	elif request.method == 'GET': 
		task = db['test_form'].find_one()
		return dumps(task) 


if __name__ == '__main__':
    app.run(debug=True)

    #curl -i -H "Content-Type: application/json" -X POST -d '{"id":5, "title": "lewl", "description": "hahahha", "done": false}' http://localhost:5000/tasks