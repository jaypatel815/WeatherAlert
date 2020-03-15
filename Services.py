# All the services that users are registered to

class EmailService:
    def __init__(self, message=None):
        self.message = message

    def update(self, message):
        self.message = message

    def __str__(self):
        return "Email Service: %s" % self.message


class smsService:
    def __init__(self, message=None):
        self.message = message

    def update(self, message):
        self.message = message

    def __str__(self):
        return "SMS Service: %s" % self.message


class PhoneService:
    def __init__(self, message=None):
        self.message = message

    def update(self, message):
        self.message = message

    def __str__(self):
        return "Phone Service: %s" % self.message
