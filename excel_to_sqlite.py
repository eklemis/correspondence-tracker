import os.path
from pathlib import Path


from databasesqlite import sqlite_cnx, sqlite_cursor

import pandas as pd

excels_dir = Path("D:\data-corr_manager")

def parsingChildrenAll():
    sql_create_childrenall_table = """ CREATE TABLE IF NOT EXISTS children_all(
        child_id text,
        full_name text NOT NULL,
        status_desc text NOT NULL,
        status_date text NOT NULL
    ) """

    sql_drop_childrenall_table = """ DROP TABLE IF EXISTS children_all """


    if sqlite_cnx is not None:
        sqlite_cursor.execute(sql_drop_childrenall_table)
        sqlite_cursor.execute(sql_create_childrenall_table)

    #retrive all data from CHILDREN_ALL.xlsx file
    childrenAllfile = os.path.join(excels_dir, "CHILDREN_ALL.xlsx")
    df = pd.read_excel(childrenAllfile, sheet_name='Sheet1')
    df = df.filter(['Child ID', 'Person Full Name', 'Status Description', 'Status Date'])
    df = df.rename(columns={"Child ID": "ChildId", "Person Full Name": "FullName", "Status Date": "StatusDate"})
    df['ChildId'] = df['ChildId'].astype(str)
    df['StatusDate'] = df['StatusDate'].astype(str)
    df = df.drop_duplicates()
    print(df.dtypes)

    #convert dataframe to tuples
    records = df.to_records(index=False)
    #put tuples to list
    result = list(records)

    #push all records to children_all table on corr_manager_local.db
    #print(result)
    sql_insertmanychildren = "INSERT INTO children_all values (?,?,?,?)"
    sqlite_cursor.executemany(sql_insertmanychildren, result)
    sqlite_cnx.commit()


def parsingMasterDonors():
    masterDonorsfile = os.path.join(excels_dir, "MASTER_DONORS.xlsx")

parsingChildrenAll()