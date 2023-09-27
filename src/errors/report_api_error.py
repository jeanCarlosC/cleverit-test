class ReportApiError(Exception):
    def __init__(self, message, data = {}, status_code=500):
        self.message = message
        self.data = data
        self.status_code = status_code
        super().__init__(self.message)