from functools import wraps
from flask import request, jsonify
from src.errors.report_api_error import ReportApiError


class input_validator:
    def __init__(self, input_structure):
        self.input_structure = input_structure

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = request.json
            print("data", data)
            # Verificar que los argumentos pasados coincidan con la estructura definida
            for rule in self.input_structure:
                field = rule["field"]
                field_type = rule["type"]
                is_required = rule["required"]
                options = rule["options"] if "options" in rule else None
                if is_required and field not in data:
                    raise ReportApiError(
                        f"El campo {field} es requerido", status_code=422)
                if field in data and not isinstance(data[field], field_type):
                    type_name = field_type.__name__
                    raise ReportApiError(
                        f"El campo {field} debe ser de tipo {type_name}", status_code=422)
                if options and data[field] not in options:
                    raise ReportApiError(
                        f"El campo {field} debe ser uno de los siguientes valores: {options}", status_code=422)

            # Llamar a la función original si los datos son válidos
            return func(*args, **kwargs)

        return wrapper
