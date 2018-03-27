from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Setting up flask',
        'description': u'We need to setup a virtual env for the flask app',
        'done': False
    },
    {
        'id': 2,
        'title': u'Creating the app.py',
        'description': u'We have to create a app.py file and use that for running the flask app',
        'done': False

    }
]

@app.route('/test/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/test/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id ]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/test/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] +1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task':task}), 201


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task  = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    task.remove(task[0])
    return jsonify({'result':True})


if (__name__) == '__main__':
    app.run(debug=False)



