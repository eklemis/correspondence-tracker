from child import Child
from donor import Donor
from databasesqlite import sqlite_cnx, sqlite_cursor

'''
sponsorship modules represent child-donor relation data
'''


class Sponsorship:
    _child = None
    _donor = None

    def __init__(self, of_child_id):
        self._child = Child(of_child_id)
        self.__pairChildDonor()

    def __pairChildDonor(self):
        sql_pair = f"select donor_id from donor_all where child_id='{self._child.getChildId()}' and spons_end_date='nan'"

        if sqlite_cnx is not None:
            sqlite_cursor.execute(sql_pair)
            record = sqlite_cursor.fetchone()
            if record:
                self._donor = Donor(record[0])
                print(f"find donor with id: {record[0]}")
            else:
                self._donor = Donor("")
        else:
            self._donor = Donor("")

    def getChild(self):
        return self._child

    def getDonor(self):
        return self._donor
