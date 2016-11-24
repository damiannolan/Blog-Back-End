#!flask/bin/python
from flask import Flask, request
import pymongo
from flask_cors import CORS, cross_origin
from bson.json_util import dumps
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)

client = pymongo.MongoClient()
db = client.test

@app.route('/people', methods=['GET', 'POST'])
def people():
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            person = request.get_json()
            db.test_form.insert_one(person)
            return 'Posted'

    elif request.method == 'GET': 
        people = []
        for person in db['test_form'].find():
            people.append(person)
        return dumps(people)

@app.route('/people/delete/<string:_id>', methods=['DELETE'])
def delete_person(_id):
    db.test_form.delete_one({'_id': ObjectId(_id)})
    return 'Deleted'
    

'''@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})'''

if __name__ == '__main__':
    app.run(debug=True)

