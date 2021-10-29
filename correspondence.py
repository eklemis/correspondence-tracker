from sponsorship import Sponsorship

class Correspondence:
    barcode = ""
    corr_number = ""
    of_child = ""
    sponsorship = None

    def __init__(self, of_child):
        self.of_child = of_child
        self.sponsorship = Sponsorship(of_child_id=self.of_child)

    def getChildId(self):
        return self.of_child