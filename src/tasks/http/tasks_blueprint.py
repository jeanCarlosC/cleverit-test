from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.tasks.usecases.tasks_usecase import tasks_usecase
from src.users.usecases.users_usecase import users_usecase
from src.frameworks.http.api_response import api_response
from src.utils.input_validator import input_validator
from src.tasks.http.fields import input_create_task, input_update_task


def create_tasks_blueprint(tasks_usecase: tasks_usecase):
    blueprint = Blueprint("tasks", __name__)


    @blueprint.route("/tasks", methods=["GET"])
    @jwt_required()
    @api_response
    def get_tasks():
        current_user = get_jwt_identity()
        print(current_user)
        data = tasks_usecase.get_tasks()
        message = "Tareas obtenidas correctamente"
        status_code = 200
        return data, message, status_code

    @blueprint.route("/tasks/<int:task_id>", methods=["GET"])
    @jwt_required()
    @api_response
    def get_task(task_id):
        data = tasks_usecase.get_task(task_id)
        message = "Tarea obtenida correctamente"
        status_code = 200
        return data, message, status_code

    @blueprint.route("/tasks", methods=["POST"])
    @jwt_required()
    @input_validator(input_create_task)
    @api_response
    def create_task():
        task = request.json
        data = tasks_usecase.create_task(task)
        message = "Tarea creada correctamente"
        status_code = 201
        return data, message, status_code

    @blueprint.route("/tasks/<int:task_id>", methods=["PUT"])
    @jwt_required()
    @input_validator(input_update_task)
    @api_response
    def update_task(task_id):
        task = request.json
        data = tasks_usecase.update_task(task_id, task)
        message = "Tarea actualizada correctamente"
        status_code = 200
        return data, message, status_code

    @blueprint.route("/tasks/<int:task_id>", methods=["DELETE"])
    @jwt_required()
    @api_response
    def delete_task(task_id):
        data = tasks_usecase.delete_task(task_id)
        message = "Tarea eliminada correctamente"
        status_code = 200
        return data, message, status_code

    return blueprint
