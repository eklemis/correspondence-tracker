import subprocess

import pandas as pd
from datetime import timedelta
from win10toast import ToastNotifier
from win10toast_click import ToastNotifier
from databasesqlite import sqlite_cnx, sqlite_cursor


class NotificationRL:

    def __init__(self):
        self.message = "Hi, \nYou have " +str(self.getCorrLate())+ " correspondence almost late (5 days left)"
        #self.message = message


    def getCorrLate(self):

        '''
        data = pd.read_excel(r'D:\data-corr_manager\CORR__LOG.xlsx')
        df = pd.DataFrame(data, columns=['corr_type_code', 'add_date'])
        df['curr_date'] = pd.to_datetime('now')
        df['rem_day'] = (df['add_date'] - df['curr_date'])
        corr_type = df.loc[(df['corr_type_code'] == 'SLC') | (df['corr_type_code'] == 'SEC')]
        rem_day = pd.Series(corr_type['rem_day']).dt.days
        rem_day = rem_day[rem_day >= -10]
        corr_type.to_excel("rem_corr_late.xlsx")
        self.temp = count(rem_day)
        return self.temp
        '''


        sql_get_remdate = f"select ((julianday(current_date) - julianday(add_date))*(-1)) as remday from corr_hist where remday >=-5"

        if sqlite_cnx is not None:
            sqlite_cursor.execute(sql_get_remdate)
            record = sqlite_cursor.fetchall()
            #for row in record :
                #print (row)

            return len(record)


    def clickableNotif(self):
        path = "D:\\data-corr_manager\\CORR_HIST.xlsx"
        subprocess.Popen([path], shell=True)
        #webbrowser.open_new(corr_late)


    def show(self):
        toast = ToastNotifier()
        toast.show_toast("Sponsorship Corr Tracker",self.message, duration=20,icon_path="icon.ico", callback_on_click=lambda :self.clickableNotif())



#notifikasi = NotificationRL("Hi,\nYou have 5 correspondence almost late (3 days left).\nPlease update their status!")
#notifikasi = NotificationRL()
#notifikasi.show()






