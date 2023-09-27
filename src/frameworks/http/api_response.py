from functools import wraps
from flask import jsonify
from src.frameworks.http.internal_code import InternalCode


def api_response(f):
    """
    Decorador para formatear la respuesta de la API
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        result = f(*args, **kwargs)
        data, message, http_code = result
        resp = format_response(data, message, http_code)
        return jsonify(resp), http_code
    return wrap


def format_response(data, message, http_code):
    return {
        "status": set_internal_code(http_code),
        "message": message,
        "data": data
    }


def set_internal_code(http_code):
    internal_code = InternalCode.SUCCESS.value
    if http_code > 299:
        internal_code = InternalCode.FAIL.value
    return internal_code
