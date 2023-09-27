from flask import Blueprint, request
from flask_restx import Api, Resource, fields
from flask_jwt_extended import jwt_required , create_access_token
from src.utils.functions import get_time_delta
from src.users.usecases.users_usecase import users_usecase
from src.frameworks.http.api_response import api_response
from src.utils.input_validator import input_validator
from src.users.http.fields import input_create_user, input_update_user, input_login_user


def create_users_blueprint(users_usecase: users_usecase):
    blueprint = Blueprint("users", __name__)

    @blueprint.route("/login", methods=["POST"])
    @input_validator(input_login_user)
    @api_response
    def login():
        user = request.json
        data_user = users_usecase.get_user(user["username"], user["password"])
        expires_delta = get_time_delta(minutes=30)
        encoded_data_user = create_access_token(identity=data_user, expires_delta=expires_delta)
        data = {"user": data_user, "access_token": encoded_data_user}
        message = "Usuario ingresado correctamente"
        status_code = 200
        return data, message, status_code

    @blueprint.route("/users/<int:user_id>", methods=["GET"])
    @jwt_required()
    @api_response
    def get_user(user_id):
        data = users_usecase.get_user(user_id)
        message = "Usuario obtenida correctamente"
        status_code = 200
        return data, message, status_code

    @blueprint.route("/users", methods=["POST"])
    @jwt_required()
    @input_validator(input_create_user)
    @api_response
    def create_user():
        user = request.json
        data = users_usecase.create_user(user)
        message = "Usuario creado correctamente"
        status_code = 201
        return data, message, status_code

    @blueprint.route("/users/<int:user_id>", methods=["PUT"])
    @jwt_required()
    @input_validator(input_update_user)
    @api_response
    def update_user(user_id):
        user = request.json
        data = users_usecase.update_user(user_id, user)
        message = "Usuario actualizado correctamente"
        status_code = 200
        return data, message, status_code

    @blueprint.route("/users/<int:user_id>", methods=["DELETE"])
    @jwt_required()
    @api_response
    def delete_user(user_id):
        data = users_usecase.delete_user(user_id)
        message = "Usuario eliminado correctamente"
        status_code = 200
        return data, message, status_code

    return blueprint
