from src.utils.validator_base import ValidatorBase
from src.errors.report_api_error import ReportApiError


class ValidatorTaskExist(ValidatorBase):
    def __init__(self, task_usecase):
        super().__init__()
        self.task_usecase = task_usecase

    def validate(self, data):
        task_id = data.get("task_id")
        response = self.task_usecase.get_task_by_id(task_id)
        if not response:
            message = f'La encuesta con id {task_id} no existe'
            data = {}
            raise ReportApiError(message, data, 404)
        data["task"] = response
        return super().validate(data)
