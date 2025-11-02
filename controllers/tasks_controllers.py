from models.tasks_models import Tasks
from db import db
from flask import make_response, request
import json


def get_tasks():
    tasks = Tasks.query.all()
    response = make_response(
        json.dumps(
            {
                "message": "All tasks retrieved successfully.",
                "data": [task.json() for task in tasks],
            },
            ensure_ascii=False,
            sort_keys=False,
        )
    )
    response.headers["Content-Type"] = "application/json"
    return response


def get_task_by_id(id):
    task = Tasks.query.get(id)

    if task:
        response = make_response(
            json.dumps(
                {"message": "Task founded with success!!", "data": task.json()},
                ensure_ascii=False,
                sort_keys=False,
            )
        )
        response.headers["Content-Type"] = "application/json"
        return response
    else:
        response = make_response(
            json.dumps(
                {"message": "Task not found.", "data": {}},
                ensure_ascii=False,
            ),
            404,
        )
        response.headers["Content-Type"] = "application/json"
        return response


def get_task_by_title(title):
    task = Tasks.query.filter_by(title=title).first()

    if task:
        response = make_response(
            json.dumps(
                {"message": "Task founded with success!!", "data": task.json()},
                ensure_ascii=False,
                sort_keys=False,
            )
        )
        response.headers["Content-Type"] = "application/json"
        return response
    else:
        response = make_response(
            json.dumps(
                {"message": "Task not found.", "data": {}},
                ensure_ascii=False,
            ),
            404,
        )
        response.headers["Content-Type"] = "application/json"
        return response


def create_task(data):
    if not all(key in data for key in ["title", "status", "description"]):
        response = make_response(
            json.dumps(
                {
                    "message": "Data invalid.",
                },
                ensure_ascii=False,
            ),
            400,
        )
        response.headers["Content-Type"] = "application/json"
        return response

    new_task = Tasks(
        title=data["title"],
        description=data["description"],
        status=data["status"],
    )

    db.session.add(new_task)
    db.session.commit()

    response = make_response(
        json.dumps(
            {"message": "Tasks created with success!!.", "data": new_task.json()},
            ensure_ascii=False,
            sort_keys=False,
        )
    )
    response.headers["Content-Type"] = "application/json"
    return response


def update_task(id, data):
    task = Tasks.query.get(id)

    if not task:
        response = make_response(
            json.dumps(
                {
                    "message": "Task not found",
                },
                ensure_ascii=False,
            ),
            404,
        )
        response.headers["Content-Type"] = "application/json"
        return response

    task.title = data["title"]
    task.description = data["description"]
    task.status = data["status"]

    db.session.commit()

    response = make_response(
        json.dumps(
            {"message": "Tasks updated with success!!.", "data": task.json()},
            ensure_ascii=False,
            sort_keys=False,
        )
    )
    response.headers["Content-Type"] = "application/json"
    return response


def remove_task(id):
    confirmation = request.args.get("confirmation")

    if confirmation != "true":
        response = make_response(
            json.dumps(
                {
                    "message": "The confirmation is required",
                },
                ensure_ascii=False,
            ),
            404,
        )
        response.headers["Content-Type"] = "application/json"
        return response

    task = Tasks.query.get(id)
    if not task:
        response = make_response(
            json.dumps(
                {
                    "message": "Task not found.",
                },
                ensure_ascii=False,
            ),
            404,
        )
        response.headers["Content-Type"] = "application/json"
        return response

    db.session.delete(task)
    db.session.commit()

    response = make_response(
        json.dumps(
            {"mensagem": "Task successfully deleted!!"},
            ensure_ascii=False,
            sort_keys=False,
        )
    )
    response.headers["Content-Type"] = "application/json"
    return response
