from src.utils.validator_base import ValidatorBase
from src.errors.report_api_error import ReportApiError


class ValidatorUserExistLogin(ValidatorBase):
    def __init__(self, user_usecase):
        super().__init__()
        self.user_usecase = user_usecase

    def validate(self, data):
        username, password = data.get("username"), data.get("password")
        response = self.user_usecase.validate_user(username, password)
        if not response:
            message = f'Usuario o contraseña incorrecta'
            data = {}
            raise ReportApiError(message, data, 401)
        data["user"] = response
        return super().validate(data)
