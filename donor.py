import pandas as pd

class Donor:
    donor_id = ""
    donor_title = ""
    donor_first = ""
    donor_middle = ""
    donor_last = ""
    donor_sufix = ""
    env_line_1 = ""
    donor_salut = ""
    adrs_line_1 = ""
    city = ""
    state_prov = ""
    country = ""
    postal_code = ""
    cmit_nbr = 0
    enr_seq = 0
    ddb_stat_code = ""
    status_date = ""

    def __init__(self, donor_id=""):
        self.donor_id = donor_id
        self.setRemainingAtributes()

    def setRemainingAtributes(self):
        base = "D:\\data-corr_manager\\"
        donor_file = base+"MASTER_DONORS.xlsx"

        df = pd.read_excel(donor_file, sheet_name='Sheet1')

        df = df[df["donor_id"] == int(self.donor_id)]
        if not df.empty:
            self.donor_title = df.iat[0,8]
            self.donor_first = df.iat[0,9]
            self.donor_middle = df.iat[0,10]
            self.donor_last = df.iat[0,11]
            self.donor_sufix = df.iat[0,12]
            self.env_line_1 = df.iat[0,2]
            self.donor_salut = df.iat[0,13]
            self.adrs_line_1 = df.iat[0,14]
            self.city = df.iat[0,17]
            self.state_prov = df.iat[0,18]
            self.country = df.iat[0,19]
            self.postal_code = df.iat[0,20]

            dce_source = base + "MASTER_ENR.xlsx"

            df = pd.read_excel(dce_source, sheet_name='Sheet1')
            df = df[df["donor_id"] == int(self.donor_id)].sort_values(by="hist_date", ascending=False)

            self.cmit_nbr = df.iat[0,2]
            self.enr_seq = df.iat[0,3]
            self.ddb_stat_code = df.iat[0,7]
            self.status_date = df.iat[0, 5]

        print(f"sponsor with name {self.getTitle()} {self.getFirstName()} created")

    def getId(self):
        return self.donor_id
    def getTitle(self):
        return self.donor_title
    def getFirstName(self):
        return self.donor_first
    def getMiddleName(self):
        return self.donor_middle
    def getLastName(self):
        return self.donor_last
    def getSufix(self):
        return self.donor_sufix
    def getEnvLineOne(self):
        return self.env_line_1
    def getCity(self):
        return self.city
    def getStateProv(self):
        return self.state_prov
    def getCountry(self):
        return self.country
    def getPostalCode(self):
        return self.postal_code
    def getDCE(self):
        return f"{self.donor_id}-{self.cmit_nbr}-{self.enr_seq}"
    def lastStatus(self):
        return self.ddb_stat_code
    def lastStatusDate(self):
        return self.status_date