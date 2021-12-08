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
    df['donor_title'] = df['donor_title'].fillna('')
    df['donor_middle'] = df['donor_middle'].fillna('')
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
    df['donor_id'] = df['donor_id'].fillna(0)
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


def parsingCorrHist() :
    sql_create_corrhist_table = """ CREATE TABLE IF NOT EXISTS corr_hist(
            donor_id text,
            corr_nbr text,
            hist_date text,
            add_date text,
            corr_stat_code text
        ) """

    sql_drop_corrhist_table = """ DROP TABLE IF EXISTS corr_hist """

    '''sql_addnewcolumn_corrhist_table = """ ALTER TABLE corr_hist
        ADD COLUMN curr_date DATE default CURRENT_DATE """ '''

    if sqlite_cnx is not None:
        sqlite_cursor.execute(sql_drop_corrhist_table)
        sqlite_cursor.execute(sql_create_corrhist_table)
        #sqlite_cursor.execute(sql_addnewcolumn_corrhist_table)

    # retrive all data from CORR_HIST.xlsx file
    corrHistfile = os.path.join(excels_dir, "CORR_HIST.xlsx")
    df = pd.read_excel(corrHistfile, sheet_name='Sheet1')
    #df['curr_date'] = pd.to_datetime('now')
    #df['rem_day']= (df['add_date'] - df['curr_date'])
    #df['rem_day'] = pd.Series(df['rem_day']).dt.days
    df = df.filter(['donor_id', 'corr_nbr', 'hist_date', 'add_date', 'corr_stat_code'])
    #df['StatusDate'] = df['StatusDate'].astype(str)
    df = df.astype(str)
    df = df.drop_duplicates()
    print(df.dtypes)

    # convert dataframe to tuples
    records = df.to_records(index=False)
    # put tuples to list
    result = list(records)

    # push all records to corr_hist table on corr_manager_local.db
    # print(result)
    sql_insertmanycorrhist = "INSERT INTO corr_hist values (?,?,?,?,?)"
    sqlite_cursor.executemany(sql_insertmanycorrhist, result)
    sqlite_cnx.commit()


def parsingCorrStatCode():
    sql_create_corrstatcode_table = """ CREATE TABLE IF NOT EXISTS corr_stat_code(
                corr_stat_code text,
                corr_stat_descr text
            ) """

    sql_drop_corrstatcode_table = """ DROP TABLE IF EXISTS corr_stat_code """

    if sqlite_cnx is not None:
        sqlite_cursor.execute(sql_drop_corrstatcode_table)
        sqlite_cursor.execute(sql_create_corrstatcode_table)

    # retrive all data from CORR_STAT_CODE.xlsx file
    corrStatCodefile = os.path.join(excels_dir, "CORR_STAT_CODE.xlsx")
    df = pd.read_excel(corrStatCodefile, sheet_name='Sheet1')
    df = df.filter(['corr_stat_code', 'corr_stat_descr'])
    # df['StatusDate'] = df['StatusDate'].astype(str)
    df = df.astype(str)
    df = df.drop_duplicates()
    print(df.dtypes)

    # convert dataframe to tuples
    records = df.to_records(index=False)
    # put tuples to list
    result = list(records)

    # push all records to corr_stat_code table on corr_manager_local.db
    # print(result)
    sql_insertmanycorrstatcode = "INSERT INTO corr_stat_code values (?,?)"
    sqlite_cursor.executemany(sql_insertmanycorrstatcode, result)
    sqlite_cnx.commit()



def parsingCorrLog():
    sql_create_corrlog_table = """ CREATE TABLE IF NOT EXISTS corr_log(
                    donor_id text,
                    corr_nbr text,
                    corr_type_code text,
                    hist_date text,
                    add_date text,
                    change_date text
                ) """

    sql_drop_corrlog_table = """ DROP TABLE IF EXISTS corr_log """

    if sqlite_cnx is not None:
        sqlite_cursor.execute(sql_drop_corrlog_table)
        sqlite_cursor.execute(sql_create_corrlog_table)

    # retrive all data from CORR__LOG.xlsx file
    corrLogfile = os.path.join(excels_dir, "CORR__LOG.xlsx")
    df = pd.read_excel(corrLogfile, sheet_name='Sheet1')
    df = df.filter(['donor_id', 'corr_nbr','corr_type_code','last_hist_date','add_date','chng_date'])
    # df['StatusDate'] = df['StatusDate'].astype(str)
    df = df.astype(str)
    df = df.drop_duplicates()
    print(df.dtypes)

    # convert dataframe to tuples
    records = df.to_records(index=False)
    # put tuples to list
    result = list(records)

    # push all records to children_all table on corr_manager_local.db
    # print(result)
    sql_insertmanycorrlog = "INSERT INTO corr_log values (?,?,?,?,?,?)"
    sqlite_cursor.executemany(sql_insertmanycorrlog, result)
    sqlite_cnx.commit()

def parsingAnotherChildrenAll():
    sql_create_antchildrenall_table = """ CREATE TABLE IF NOT EXISTS ant_childrenall(
                        child_id text,
                        full_name text NOT NULL,
                        school_name text
                    ) """

    sql_drop_antchildrenall_table = """ DROP TABLE IF EXISTS ant_childrenall """

    if sqlite_cnx is not None:
        sqlite_cursor.execute(sql_drop_antchildrenall_table)
        sqlite_cursor.execute(sql_create_antchildrenall_table)

    # retrive all data from CHILDREN_ALL.xlsx file
    antChildrenAllfile = os.path.join(excels_dir, "CHILDREN_ALL.xlsx")
    df = pd.read_excel(antChildrenAllfile, sheet_name='Sheet1')
    df = df.filter(['Child ID', 'Person Full Name', 'School Name'])
    # df['StatusDate'] = df['StatusDate'].astype(str)
    df = df.astype(str)
    df = df.drop_duplicates()
    print(df.dtypes)

    # convert dataframe to tuples
    records = df.to_records(index=False)
    # put tuples to list
    result = list(records)

    # push all records to children_all table on corr_manager_local.db
    # print(result)
    sql_insertmanyantchildall = "INSERT INTO ant_childrenall values (?,?,?)"
    sqlite_cursor.executemany(sql_insertmanyantchildall, result)
    sqlite_cnx.commit()


def parsingAntDonorAll():
    sql_create_antdonorall_table = """ CREATE TABLE IF NOT EXISTS ant_donorall (
            child_id text,
            donor_id text,
            dce_num text,
            donor_name text 
        ) """

    sql_drop_antdonorall_table = """ DROP TABLE IF EXISTS ant_donorall """

    if sqlite_cnx is not None:
        sqlite_cursor.execute(sql_drop_antdonorall_table)
        sqlite_cursor.execute(sql_create_antdonorall_table)

    antDonorAllfile = os.path.join(excels_dir, "DONOR_ALL.xlsx")
    df = pd.read_excel(antDonorAllfile, sheet_name='Sheet1')
    df = df.filter(['child_id', 'donor_id', 'DCE_Number', 'env_line_1'])
    # remove NaN values
    df['donor_id'] = df['donor_id'].fillna(0)
    df['donor_id'] = df['donor_id'].astype(int)
    df = df.astype(str)
    df.drop_duplicates()

    # convert dataframe to tuples
    records = df.to_records(index=False)
    # put tuples to list
    result = list(records)

    sql_insertmanyantdonorall = "INSERT INTO ant_donorall values (?,?,?,?)"
    sqlite_cursor.executemany(sql_insertmanyantdonorall, result)
    sqlite_cnx.commit()

parsingChildrenAll()
parsingMasterDonors()
parsingMasterEnr()
parsingDonorAll()
parsingCorrHist()
parsingCorrStatCode()
parsingCorrLog()
parsingAnotherChildrenAll()
parsingAntDonorAll()