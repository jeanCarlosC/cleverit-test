from src.utils.validator_base import ValidatorBase
from src.errors.report_api_error import ReportApiError


class ValidatorUserExist(ValidatorBase):
    def __init__(self, user_usecase):
        super().__init__()
        self.user_usecase = user_usecase

    def validate(self, data):
        id = data.get("user_id")
        response = self.user_usecase.get_user_by_id(id)
        if not response:
            message = f'Usuario con id {id} no existe'
            data = {}
            raise ReportApiError(message, data, 404)
        data["user"] = response
        return super().validate(data)
