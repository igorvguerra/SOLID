from .notificator_interface import NotificatorInterface

class ClientService:
    def __init__(self, notificator: NotificatorInterface):
        self.notificator = notificator

    def send(self, message: str):
        self.notificator.send_notification(message)