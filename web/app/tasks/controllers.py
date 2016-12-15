# coding=utf-8

from flask import jsonify, request, abort, Blueprint
from werkzeug.exceptions import NotFound

from models import db, Task
from app.snippets import get_object_or_404

tasks = Blueprint('tasks', __name__)


@tasks.route('/', methods=['GET'])
def get_tasks():
    task_list = [
        task.serialize()
        for task
        in Task.query.limit(50).all()
    ]
    return jsonify(task_list)


@tasks.route('/', methods=['POST'])
def create_task():
    try:
        task = Task.create(**request.json)
        db.session.add(task)
        db.session.commit()
        return jsonify(task.serialize()), 201
    except Exception as err:
        abort(400, description=err)


@tasks.route('/<task_id>', methods=['GET'])
def get_task(task_id):
    task = get_object_or_404(Task, Task.id == task_id)
    return jsonify(task.serialize())


@tasks.route('/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        task = get_object_or_404(Task, Task.id == task_id)
        db.session.delete(task)
        db.session.commit()
        return jsonify({}), 204
    except NotFound:
        raise
    except Exception as err:
        abort(400, description=err)

