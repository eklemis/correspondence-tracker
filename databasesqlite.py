import sqlite3

sqlite_cnx = sqlite3.connect('corr_manager_local.db')
sqlite_cursor = sqlite_cnx.cursor()