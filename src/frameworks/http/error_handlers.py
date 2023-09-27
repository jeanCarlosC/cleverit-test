import logging
import json
from flask import jsonify
from src.errors.report_api_error import ReportApiError
from src.frameworks.http.internal_code import InternalCode


def Error_handler(e):

    """
    Manejador de errores para excepciones no controladas en la aplicación.
    """

    message = "Internal error during request."
    status_code = 500
    data = {}

    if e.__class__.__name__ == "NotFound":
        message = "Recurso no encontrado."
        status_code = 404
    if e.__class__.__name__ == "MethodNotAllowed":
        message = "Método no permitido."
        status_code = 405
    
    logging.exception(e)

    response = {
        "status": "failed",
        "message": message,
        "data": data,
    }

    return jsonify(response), status_code


def report_api_error_handler(exc: ReportApiError):
    return handle_logic_error(exc.message, exc.status_code, exc.data)


def handle_logic_error(message, status_code, data = {}):
    """
    Manejador de errores para excepciones que no retornen un 500.
    Ya que es un error lógico, no se debe mostrar el stack trace.
    """
    content = {
        "status": InternalCode.FAIL.value,
        "message": message,
        "data": data,
    }
    print(content)
    return jsonify(content), status_code