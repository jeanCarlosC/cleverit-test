from src.utils.validator_base import ValidatorBase
from src.errors.report_api_error import ReportApiError


class ValidatorTaskExistData(ValidatorBase):
    def __init__(self, task_usecase):
        super().__init__()
        self.task_usecase = task_usecase

    def validate(self, data):
        title, user_id = data.get("title"), data.get("user_id")
        response = self.task_usecase.get_task_by_title(title)
        if response:
            message = f"La encuesta con titulo '{title}' ya existe"
            data = {}
            raise ReportApiError(message, data, 422)
        if user_id:
            response = self.task_usecase.get_user_by_id(user_id)
            if not response:
                message = f"El usuario con id '{user_id}' no existe"
                data = {}
                raise ReportApiError(message, data, 422)
        data["task"] = response
        return super().validate(data)
