import subprocess

import pandas as pd
from datetime import timedelta
from win10toast import ToastNotifier
from win10toast_click import ToastNotifier
from databasesqlite import sqlite_cnx, sqlite_cursor


class Notification:

    def __init__(self):
        self.message = "Hi, \nYou have " +str(self.getRLLate())+ " RL and "+str(self.getTDLLate())+" TDL almost late (5 days left).\n Click here to update!"


    def getRLLate(self):

        sql_get_rllate = f"select ant_childrenall.school_name, ant_childrenall.full_name, ant_childrenall.child_id, corr_hist.donor_id, corr_hist.hist_date, corr_stat_code.corr_stat_descr, corr_hist.corr_nbr, " \
                         f"((julianday(current_date)-(julianday(corr_log.add_date)+28))*(-1)) as days_late " \
                         f"from ant_childrenall join ant_donorall on ant_childrenall.child_id = ant_donorall.child_id " \
                         f"join corr_log on ant_donorall.donor_id = corr_log.donor_id " \
                         f"join corr_hist on corr_log.corr_nbr = corr_hist.corr_nbr " \
                         f"join corr_stat_code on corr_hist.corr_stat_code = corr_stat_code.corr_stat_code " \
                         f"where days_late >= -6 and corr_log.corr_type_code in ('SLC', 'SEC' ) " \
                         f"and corr_hist.corr_stat_code not in ('I','K','L','Z')"


        if sqlite_cnx is not None:
            sqlite_cursor.execute(sql_get_rllate)
            columns = [desc[0] for desc in sqlite_cursor.description]
            record = sqlite_cursor.fetchall()
            df = pd.DataFrame(list(record), columns=columns)
            writer = pd.ExcelWriter('D:\\data-corr_manager\\Book Entry RL.xlsx')
            df.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            #for row in record :
                #print (row)

            return len(record)


    def getTDLLate(self):
        sql_get_tdllate = f"select ant_childrenall.child_id, ant_childrenall.full_name, ant_donorall.donor_name, ant_donorall.dce_num, " \
                         f"((julianday(current_date)-(julianday(corr_log.add_date)+28))*(-1)) as days_late " \
                         f"from ant_childrenall join ant_donorall on ant_childrenall.child_id = ant_donorall.child_id " \
                         f"join corr_log on ant_donorall.donor_id = corr_log.donor_id " \
                         f"join corr_hist on corr_log.corr_nbr = corr_hist.corr_nbr " \
                         f"join corr_stat_code on corr_hist.corr_stat_code = corr_stat_code.corr_stat_code " \
                         f"where days_late >= -6 and corr_log.corr_type_code = 'WLS' " \
                         f"and corr_hist.corr_stat_code not in ('I','K','L','Z')"

        if sqlite_cnx is not None:
            sqlite_cursor.execute(sql_get_tdllate)
            columns = [desc[0] for desc in sqlite_cursor.description]
            record = sqlite_cursor.fetchall()
            df = pd.DataFrame(list(record), columns=columns)
            writer = pd.ExcelWriter('D:\\data-corr_manager\\Book Entry TDL.xlsx')
            df.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            #for row in record :
                #print (row)

            return len(record)


    def clickableNotif(self):
        path = "D:\\data-corr_manager\\Book Entry RL.xlsx"
        subprocess.Popen([path], shell=True)
        #webbrowser.open_new(corr_late)


    def show(self):
        toast = ToastNotifier()
        toast.show_toast("Sponsorship Corr Tracker",self.message, duration=20,icon_path="icon.ico", callback_on_click=lambda :self.clickableNotif())



notifikasi = Notification()
notifikasi.show()
#notifikasi.getRLLate()
#notifikasi.getTDLLate()






