import webbrowser

import pandas as pd
from datetime import timedelta
from win10toast import ToastNotifier
from win10toast_click import ToastNotifier


class NotificationRL:
    def __init__(self):
        self.message = "Hi, \nYou have " +str(self.getCorrLate())+ " correspondence almost late (10 days left)"

    def getCorrLate(self):
        data = pd.read_excel(r'D:\data-corr_manager\CORR__LOG.xlsx')
        df = pd.DataFrame(data, columns=['corr_type_code', 'add_date'])
        df['curr_date'] = pd.to_datetime('now')
        df['rem_day'] = (df['add_date'] - df['curr_date'])
        corr_type = df.loc[(df['corr_type_code'] == 'SLC') | (df['corr_type_code'] == 'SEC')]
        rem_day = pd.Series(corr_type['rem_day']).dt.days
        rem_day = rem_day[rem_day >= -10]
        corr_type.to_excel("rem_corr_late.xlsx")
        self.temp = len(rem_day)
        return self.temp

    def clickableNotif(self):
        corr_late = "rem_corr_late.xlsx"
        webbrowser.open_new(corr_late)


    def show(self):
        toast = ToastNotifier()
        toast.show_toast("Sponsorship Corr Tracker",self.message, duration=20,icon_path="icon.ico", callback_on_click=lambda :self.clickableNotif())


notifikasi = NotificationRL()
notifikasi.show()




