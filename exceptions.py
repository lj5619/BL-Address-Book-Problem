class ValidationError(Exception):
    def __init__(self, message):
        self.msg = message
    
    def __str__(self):
        return self.msg
