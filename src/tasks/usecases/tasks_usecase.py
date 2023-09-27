
from src.utils.create_validator_chain import create_validator_chain
from src.tasks.validators.validator_task_exist import ValidatorTaskExist
from src.tasks.validators.validator_task_exist_data import ValidatorTaskExistData


class tasks_usecase:
    def __init__(self, sqliteRepository, sqliteRepositoryUser):
        self.sqliteRepository = sqliteRepository
        self.sqliteRepositoryUser = sqliteRepositoryUser

    def get_tasks(self):
        return self.sqliteRepository.get_tasks()

    def get_task(self, task_id):
        main_validator = create_validator_chain([
            ValidatorTaskExist(self),
        ])
        response = main_validator.validate({"task_id": task_id})
        return response["task"]

    def get_task_by_id(self, task_id):
        return self.sqliteRepository.get_task(task_id)

    def get_task_by_title(self, title):
        return self.sqliteRepository.get_task_by_title(title)

    def create_task(self, task):
        main_validator = create_validator_chain([
            ValidatorTaskExistData(self),
        ])
        main_validator.validate(task)
        return self.sqliteRepository.create_task(task)

    def update_task(self, task_id, task):
        main_validator = create_validator_chain([
            ValidatorTaskExist(self),
            ValidatorTaskExistData(self),
        ])
        main_validator.validate({"task_id": task_id, **task})
        return self.sqliteRepository.update_task(task_id, task)

    def delete_task(self, task_id):
        main_validator = create_validator_chain([
            ValidatorTaskExist(self),
        ])
        main_validator.validate({"task_id": task_id})
        return self.sqliteRepository.delete_task(task_id)

    def get_user_by_id(self, user_id):
        return self.sqliteRepositoryUser.get_by_id(user_id)
