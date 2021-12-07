import subprocess

import pandas as pd
from datetime import timedelta
from win10toast import ToastNotifier
from win10toast_click import ToastNotifier
from databasesqlite import sqlite_cnx, sqlite_cursor


class NotificationRL:

    def __init__(self):
        self.message = "Hi, \nYou have " +str(self.getCorrLate())+ " correspondence almost late (5 days left) \nClick here to update!"


    def getCorrLate(self):

        sql_get_remdate = f"select children_all.full_name, children_all.child_id, corr_hist.donor_id, corr_hist.hist_date, corr_stat_code.corr_stat_descr, corr_hist.corr_nbr, " \
                          f"((julianday(add_date)+28)-julianday(current_date)) as days_late " \
                          f"from children_all join donor_all on children_all.child_id = donor_all.child_id " \
                          f"join corr_hist on donor_all.donor_id = corr_hist.donor_id " \
                          f"join corr_stat_code on corr_hist.corr_stat_code = corr_stat_code.corr_stat_code " \
                          f"where days_late >= -6 and corr_hist.corr_stat_code not in ('I','K','L','Z')"


        if sqlite_cnx is not None:
            sqlite_cursor.execute(sql_get_remdate)
            columns = [desc[0] for desc in sqlite_cursor.description]
            record = sqlite_cursor.fetchall()
            df = pd.DataFrame(list(record), columns=columns)
            writer = pd.ExcelWriter('D:\\data-corr_manager\\Book Entry.xlsx')
            df.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            #for row in record :
                #print (row)

            return len(record)


    def clickableNotif(self):
        path = "D:\\data-corr_manager\\Book Entry.xlsx"
        subprocess.Popen([path], shell=True)
        #webbrowser.open_new(corr_late)


    def show(self):
        toast = ToastNotifier()
        toast.show_toast("Sponsorship Corr Tracker",self.message, duration=20,icon_path="icon.ico", callback_on_click=lambda :self.clickableNotif())



#notifikasi = NotificationRL()
#notifikasi.show()






