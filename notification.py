from win10toast import ToastNotifier

class Notification:
    def __init__(self, message):
        self.message = message
    def show_notif(self):
        toast = ToastNotifier()
        toast.show_toast("Sponsorship Corr Tracker",self.message, duration=20,icon_path="icon.ico")
