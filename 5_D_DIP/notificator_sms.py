from .notificator_interface import NotificatorInterface

class NotificatiorSms(NotificatorInterface):
    def send_notification(self, message: str): 
        print(f"Sending SMS: {message}")