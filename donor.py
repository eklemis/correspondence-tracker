import pandas as pd

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
        donor_file = base+"MASTER_DONORS.xlsx"

        df = pd.read_excel(donor_file, sheet_name='Sheet1')
        if self._donor_id == "":
            self._donor_id = "0"
        df = df[df["donor_id"] == int(self._donor_id)]
        if not df.empty:
            self._donor_title = df.iat[0,8]
            self._donor_first = df.iat[0,9]
            self._donor_middle = df.iat[0,10]
            self._donor_last = df.iat[0,11]
            self._donor_sufix = df.iat[0,12]
            self._env_line_1 = df.iat[0,2]
            self._donor_salut = df.iat[0,13]
            self._adrs_line_1 = df.iat[0,14]
            self._city = df.iat[0,17]
            self._state_prov = df.iat[0,18]
            self._country = df.iat[0,19]
            self._postal_code = df.iat[0,20]

            dce_source = base + "MASTER_ENR.xlsx"

            df = pd.read_excel(dce_source, sheet_name='Sheet1')
            df = df[df["donor_id"] == int(self._donor_id)].sort_values(by="hist_date", ascending=False)

            self._cmit_nbr = df.iat[0,2]
            self._enr_seq = df.iat[0,3]
            self._ddb_stat_code = df.iat[0,7]
            self._status_date = df.iat[0, 5]

        print(f"sponsor with name {self.getTitle()} {self.getFirstName()} created")

    def getId(self):
        return self._donor_id
    def getTitle(self):
        return self._donor_title
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