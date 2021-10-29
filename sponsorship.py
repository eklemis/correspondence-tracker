import pandas as pd

from child import Child
from donor import Donor

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
        base = "D:\\data-corr_manager\\"
        sponsorship_file = base + "DONOR_ALL.xlsx"

        df = pd.read_excel(sponsorship_file, sheet_name='Sheet1')
        del df["country"]
        del df["Phone"]
        del df["postal_code"]
        del df["state_prov"]
        del df["city"]
        del df["adrs_line_3"]
        del df["adrs_line_2"]
        del df["adrs_line_1"]

        df = df[(df["child_id"] == int(self._child.getChildId())) & (df["Spons_End_Date"].isnull())]
        if not df.empty:
            self._donor = Donor(str(int(df.iat[0, 13])))
        else:
            self._donor = Donor("")

    def getChild(self):
        return self._child

    def getDonor(self):
        return self._donor
