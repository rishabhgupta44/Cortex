# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import os
import sqlite3
import sys


"""
 This script will help me to make andcontinue my scedules 

"""

def dbManager():
    Connection = sqlite3.connect("Database/scedule.db")
    NewConneection = Connection.cursor()
    AN = NewConneection.execute("CREATE TABLE scedule(ID INT(25) PRIMARY KEY,D CHAR(255),T CHAR(122)) ") 
    if(AN):
        print("success")
    else:
        print("fail")    

def data():
    Connection = sqlite3.connect("Database/scedule.db")
    NewConneection = Connection.cursor()
    New = NewConneection.execute("SELECT * FROM scedule")
    Data = New.fetchall()
    print(Data)

def InsertData(day,time):
    Connection = sqlite3.connect("Database/scedule.db")
    NewConnection = Connection.cursor()
    New = NewConnection.execute("INSERT INTO scedule(ID,D,T) VALUES(1,12,13)")
    if (New):
        print("Added Successfully")
    else:
        print("Failed")
    Connection.close()

data()