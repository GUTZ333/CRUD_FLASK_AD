from controllers.tasks_controllers import create_task, get_task_by_id, get_tasks, remove_task, update_task, get_task_by_title
from flask import Blueprint, request

task_routes = Blueprint("tasks_routes", __name__)

@task_routes.route("/tasks", methods=["GET"])
def handler_get_tasks():
    return get_tasks()

@task_routes.route("/task/<int:id>", methods=["GET"])
def handler_get_task_by_id(id):
    return get_task_by_id(id)

@task_routes.route("/task/<string:title>", methods=["GET"])
def handler_get_task_by_title(title):
    return get_task_by_title(title)

@task_routes.route("/post_task", methods=["POST"])
def handler_post_task():
    data = request.json
    return create_task(data)

@task_routes.route("/put_task/<int:id>", methods=["PUT"])
def handler_put_task(id):
    data = request.json
    return update_task(id, data)

@task_routes.route("/delete_task/<int:id>", methods=["DELETE"])
def handler_delete_task(id):
    return remove_task(id)