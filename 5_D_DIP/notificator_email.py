from .notificator_interface import NotificatorInterface

class NotificatiorEmail(NotificatorInterface):
    def send_notification(self, message: str): 
        print(f"Sending Email: {message}")