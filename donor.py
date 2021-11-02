import pandas as pd
from databasesqlite import sqlite_cnx, sqlite_cursor

class Donor:
    _donor_id = ""
    _donor_title = ""
    _donor_first = ""
    _donor_middle = ""
    _donor_last = ""
    _donor_sufix = ""
    _env_line_1 = ""
    _donor_salut = ""
    _adrs_line_1 = ""
    _city = ""
    _state_prov = ""
    _country = ""
    _postal_code = ""
    _cmit_nbr = 0
    _enr_seq = 0
    _ddb_stat_code = ""
    _status_date = ""

    def __init__(self, donor_id=""):
        self._donor_id = donor_id
        self.setRemainingAtributes()

    def setRemainingAtributes(self):
        base = "D:\\data-corr_manager\\"

        sql_get_donor = f"select * from master_donor join master_enr on master_donor.donor_id=master_enr.donor_id where master_donor.donor_id='{self._donor_id}'"
        if sqlite_cnx is not None:
            sqlite_cursor.execute(sql_get_donor)
            record = sqlite_cursor.fetchone()
            print(record)
            if len(record) > 0:
                self._donor_title = record[1]
                self._donor_first = record[2]
                self._donor_middle = record[3]
                self._donor_last = record[4]
                self._donor_sufix = record[5]
                self._env_line_1 = record[6]
                self._donor_salut = record[7]
                self._adrs_line_1 = record[8]
                self._city = record[9]
                self._state_prov = record[10]
                self._country = record[11]
                self._postal_code = record[12]

                self._cmit_nbr = record[13]
                self._enr_seq = record[14]
                self._ddb_stat_code = record[15]
                self._status_date = record[16]

                '''dce_source = base + "MASTER_ENR.xlsx"

                df = pd.read_excel(dce_source, sheet_name='Sheet1')
                df = df[df["donor_id"] == int(self._donor_id)].sort_values(by="hist_date", ascending=False)

                self._cmit_nbr = df.iat[0,2]
                self._enr_seq = df.iat[0,3]
                self._ddb_stat_code = df.iat[0,7]
                self._status_date = df.iat[0, 5]'''

                print(f"sponsor with name {self.getTitleFirstName()} created")

    def getId(self):
        return self._donor_id
    def getTitle(self):
        return self._donor_title
    def getTitleFirstName(self):
        return f"{self._donor_title} {self._donor_first}"
    def getFirstName(self):
        return self._donor_first
    def getMiddleName(self):
        return self._donor_middle
    def getLastName(self):
        return self._donor_last
    def getSufix(self):
        return self._donor_sufix
    def getEnvLineOne(self):
        return self._env_line_1
    def getCity(self):
        return self._city
    def getStateProv(self):
        return self._state_prov
    def getCountry(self):
        return self._country
    def getPostalCode(self):
        return self._postal_code
    def getDCE(self):
        return f"{self._donor_id}-{self._cmit_nbr}-{self._enr_seq}"
    def lastStatus(self):
        return self._ddb_stat_code
    def lastStatusDate(self):
        return self._status_date