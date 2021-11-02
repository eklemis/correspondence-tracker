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
    sql_create_donorall_table = """ CREATE TABLE IF NOT EXISTS master_donor (
        donor_id text primary key,
        donor_title text,
        donor_first text not null,
        donor_middle text,
        donor_last text,
        donor_sufix text,
        env_line_1 text,
        donor_salut text,
        adrs_line_1 text,
        city text,
        state_prov text,
        country text,
        postal_code text
    ) """

    sql_drop_donorall_table = """ DROP TABLE IF EXISTS master_donor """

    if sqlite_cnx is not None:
        sqlite_cursor.execute(sql_drop_donorall_table)
        sqlite_cursor.execute(sql_create_donorall_table)

    masterDonorsfile = os.path.join(excels_dir, "MASTER_DONORS.xlsx")
    df = pd.read_excel(masterDonorsfile, sheet_name='Sheet1')
    df = df.filter(['donor_id','donor_title','donor_first','donor_middle','donor_last','donor_suffix','env_line_1','donor_salut','adrs_line_1','city','state_prov','country','postal_code'])
    df = df.dropna(subset=['donor_title'])
    df = df.dropna(subset=['donor_middle'])
    df = df.astype(str)
    df.drop_duplicates()

    # convert dataframe to tuples
    records = df.to_records(index=False)
    # put tuples to list
    result = list(records)

    # push all records to children_all table on corr_manager_local.db
    sql_insertmanychildren = "INSERT INTO master_donor values (?,?,?,?,?,?,?,?,?,?,?,?,?)"
    sqlite_cursor.executemany(sql_insertmanychildren, result)
    sqlite_cnx.commit()


def parsingMasterEnr():
    sql_create_masterenr_table = """ CREATE TABLE IF NOT EXISTS master_enr (
    donor_id text,
    cmit_nbr text,
    enr_seq text,
    seq_nbr text,
    hist_date text,
    ddb_stat_code text
    ) """

    sql_drop_masterenr_table = """ DROP TABLE IF EXISTS master_enr """

    if sqlite_cnx is not None:
        sqlite_cursor.execute(sql_drop_masterenr_table)
        sqlite_cursor.execute(sql_create_masterenr_table)

    masterEnrfile = os.path.join(excels_dir, "MASTER_ENR.xlsx")
    df = pd.read_excel(masterEnrfile, sheet_name='Sheet1')
    df = df.filter(['donor_id','cmit_nbr','enr_seq','seq_nbr','hist_date','ddb_stat_code'])
    df = df.astype(str)
    df.drop_duplicates()

    # convert dataframe to tuples
    records = df.to_records(index=False)
    # put tuples to list
    result = list(records)

    # push all records to master_enr table on corr_manager_local.db
    sql_insertmanymsterener = "INSERT INTO master_enr values (?,?,?,?,?,?)"
    sqlite_cursor.executemany(sql_insertmanymsterener, result)
    sqlite_cnx.commit()

def parsingDonorAll():
    sql_create_donorall_table = """ CREATE TABLE IF NOT EXISTS donor_all (
        child_id text,
        donor_id text,
        spons_start_date text,
        spons_end_date text,
        enr_type_code text,
        ddb_stat_code text 
    ) """

    sql_drop_donorall_table = """ DROP TABLE IF EXISTS donor_all """

    if sqlite_cnx is not None:
        sqlite_cursor.execute(sql_drop_donorall_table)
        sqlite_cursor.execute(sql_create_donorall_table)

    donorAllfile = os.path.join(excels_dir, "DONOR_ALL.xlsx")
    df = pd.read_excel(donorAllfile, sheet_name='Sheet1')
    df = df.filter(['child_id','donor_id','Spons_Start_Date','Spons_End_Date','enr_type_code','ddb_stat_code'])
    #remove NaN values
    df = df.dropna(subset=['donor_id'])
    df['donor_id'] = df['donor_id'].astype(int)
    df = df.astype(str)
    df.drop_duplicates()

    # convert dataframe to tuples
    records = df.to_records(index=False)
    # put tuples to list
    result = list(records)

    sql_insertmanydonorall = "INSERT INTO donor_all values (?,?,?,?,?,?)"
    sqlite_cursor.executemany(sql_insertmanydonorall,result)
    sqlite_cnx.commit()

parsingChildrenAll()
parsingMasterDonors()
parsingMasterEnr()
parsingDonorAll()