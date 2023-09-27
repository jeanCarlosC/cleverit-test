
from src.utils.create_validator_chain import create_validator_chain
from src.users.validators.validator_user_exist_login import ValidatorUserExistLogin
from src.users.validators.validator_user_exist import ValidatorUserExist
class users_usecase:
    def __init__(self, sqliteRepository):
        self.sqliteRepository = sqliteRepository

    def get_user(self, username, password):
        main_validator = create_validator_chain([
            ValidatorUserExistLogin(self),
        ])
        data = main_validator.validate({"username": username, "password": password})
        return data["user"]
    
    def validate_user(self, username, password):
        return self.sqliteRepository.validate_user(username, password)
    
    def get_user_by_id(self, user_id):
        return self.sqliteRepository.get_by_id(user_id)

    def create_user(self, user):
        print(user)
        return self.sqliteRepository.create_user(user)

    def update_user(self, user_id, user):
        main_validator = create_validator_chain([
            ValidatorUserExist(self),
        ])
        main_validator.validate({"user_id": user_id})
        return self.sqliteRepository.update_user(user_id, user)
    
    def delete_user(self, user_id):
        main_validator = create_validator_chain([
            ValidatorUserExist(self),
        ])
        main_validator.validate({"user_id": user_id})
        return self.sqliteRepository.delete_user(user_id)