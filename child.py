import pandas as pd

class Child:
    child_id = ""
    child_name = ""
    latest_status = ""
    status_date = ""
    def __init__(self, id):
        self.child_id = id
        self.setRemainingAttributes()

    def setRemainingAttributes(self):
        base = "D:\\data-corr_manager\\"
        children_file = base+"CHILDREN_ALL.xlsx"

        df = pd.read_excel(children_file, sheet_name='Sheet1')
        df = df.filter(['Child ID','Person Full Name','Status Description','Status Date'])
        df = df.rename(columns = {"Child ID": "ChildId", "Person Full Name": "FullName", "Status Date":"StatusDate"})

        df = df[df["ChildId"] == int(self.child_id)]
        if not df.empty:
            self.child_name = df.iat[0,1]
            self.latest_status = df.iat[0,2]
            self.status_date = df.iat[0,3]

        print(f"a child name :{self.getFirstName()} has been created")

    def setId(self, id):
        self.child_id = id

    def setName(self, name):
        self.child_name = name

    def getStatus(self):
        return self.latest_status
    def getChildId(self):
        return self.child_id
    def getFirstName(self):
        #only return child first name
        #if first name only have 1 letter, return first name+next word in the name
        names = self.child_name.split(" ")
        if len(names) > 0:
            if not len(names[0]) == 1:
                return names[0]
            else:
                if len(names) > 1:
                    return names[0]+" "+names[1]
        return ""
