class ValidatorBase():
    def __init__(self):
        self.next = None

    def set_next(self, next_validator):
        self.next = next_validator

    def validate(self, data):
        if self.next is not None:
            return self.next.validate(data)
        return data
    def validate_update(self, data):
        if self.next is not None:
            return self.next.validate_update(data)
        return data
