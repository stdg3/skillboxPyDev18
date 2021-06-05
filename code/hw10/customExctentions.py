class IamGodError(Exception):
    def __init__(self, message="i am god"):
        self.message = message
    
    def __str__(self):
        return self.message


class DrunkError(Exception):
    def __init__(self, message="i am drunk"):
        self.message = message
    
    def __str__(self):
        return self.message


class CarCrashError(Exception):
    def __init__(self, message="car crash err"):
        self.message = message
    
    def __str__(self):
        return self.message


class GluttonyError(Exception):
    def __init__(self, message="i am glutton"):
        self.message = message
    
    def __str__(self):
        return self.message


class DepressionError(Exception):
    def __init__(self, message="depressive err"):
        self.message = message
    
    def __str__(self):
        return self.message


class SuicideError(Exception):
    def __init__(self, message="the end"):
        self.message = message
    
    def __str__(self):
        return self.message
