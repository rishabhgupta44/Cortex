# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

#here i will create modules for whole pc diagnostics
import os, sys, json, sqlite3, pprint
#pc charger details
db = os.path.join("Database/", "CDetails.db")
Cursor = sqlite3.connect(db)
CCursour = Cursor.cursor()


def SERVICE_START():
    db = os.path.join("Database/", "CDetails.db")
    Cursor = sqlite3.connect(db)
    CCursour = Cursor.cursor()


#Exec = CCursour.execute("CREATE TABLE CList(ListID integer AUTO_INCREMENT NOT NULL PRIMARY KEY, CheckDate VARCHAR(255))")
#Exec = CCursour.execute("DROP TABLE CList")
MAX_NUM = vExec = CCursour.execute("SELECT max(ListID) FROM CList")
MAX_CALL = vExec.fetchall()


class DBManager:
    def __init__(self):
        self.db = db


def INVOKE_MAX_CALL():

    Cursor = sqlite3.connect(db)
    CCursour = Cursor.cursor()
    MAX_NUM = vExec = CCursour.execute("SELECT max(ListID) FROM CList")
    MAX_CALL = vExec.fetchall()
    return MAX_CALL


def InsertTable(CreatorDate):
    try:
        MAX_CALL = INVOKE_MAX_CALL()

        IDNum = int(MAX_CALL[len(MAX_CALL) - 1][0]) + 1
    except:
        IDNum = 1
    Exec = CCursour.execute(
        f"INSERT INTO CList VALUES({IDNum},{str(CreatorDate)})")
    Cursor.commit()
    Cursor.close()
    Exec = CCursour.execute("TRUNCATE FROM CList")
    Cursor.commit()
    Cursor.close()


v = CCursour.execute("SELECT * FROM CList")
m = v.fetchall()
pprint.pprint(m)


def CCheckACTIVE():
    import psutil, time
    battery = psutil.sensors_battery()
    stat = battery.power_plugged
    percentage = battery.percent
    if stat == True:
        try:
            return 1
            #InsertTable(str(time.time()))
            #print("inserted")
        except:
            pass
    else:
        if stat == False:
            return 0


def ChargeList():
    while True:
        m = CCheckACTIVE()
        if m == 0:
            Cursor = sqlite3.connect(db)
            CCursour = Cursor.cursor()
        if m == 1:
            try:
                import time
                InsertTable(time.time())
            except:
                pass
