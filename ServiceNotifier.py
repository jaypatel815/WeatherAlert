from Services import *

class ServiceNotifier:
    def __init__(self, pService=None):
        self.pService = pService
        self.Services = []

    def attach(self, pService):
        # Adds service to the current Array
        self.Services.append(pService)

    def detach(self, pService):
        # Removes service
        self.Services.remove(pService)

    def ServiceNotifier(self, message):
        # For each service in array of services update the message
        if self.Services:
            for service in self.Services:
                service.update(message)


def main():
    # Driver function to test all the services
    notification = ServiceNotifier()

    phone = PhoneService()
    sms = smsService()
    email = EmailService()

    notification.attach(phone)
    notification.attach(email)
    notification.attach(sms)

    notification.ServiceNotifier("Weather Alert Works!")

    print(phone)
    print(sms)
    print(email)


if __name__ == "__main__":
    # Runs the driver function and checks to see if it is working properly
    main()
