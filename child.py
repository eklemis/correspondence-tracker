import pandas as pd
from databasesqlite import sqlite_cnx, sqlite_cursor

class Child:
    _child_id = ""
    _child_name = ""
    _latest_status = ""
    _status_date = ""
    def __init__(self, id):
        self._child_id = id
        self.setRemainingAttributes()

    def setRemainingAttributes(self):
        sql_get_child = f"select * from children_all where child_id='{self.getChildId()}'"

        if sqlite_cnx is not None:
            sqlite_cursor.execute(sql_get_child)
            record = sqlite_cursor.fetchone()
            if record:
                self._child_name = record[1]
                self._latest_status = record[2]
                self._status_date = record[3]

    def setId(self, id):
        self._child_id = id

    def setName(self, name):
        self._child_name = name

    def getStatus(self):
        return self._latest_status
    def getChildId(self):
        return self._child_id
    def getFirstName(self):
        #only return child first name
        #if first name only have 1 letter, return first name+next word in the name
        names = self._child_name.split(" ")
        if len(names) > 0:
            if not len(names[0]) == 1:
                return names[0]
            else:
                if len(names) > 1:
                    return names[0]+" "+names[1]
        return ""