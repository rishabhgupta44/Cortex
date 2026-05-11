# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import os
import time
import json

import mysql.connector
import sys

hostname = 'localhost'
username = 'root'
password = 'flashdc100'
database = 'Cortex'
connection = mysql.connector.connect(
    host=hostname, user=username, passwd=password, db=database)
cursor = connection.cursor()
query = ("INSERT INTO logs(ID,time,name) VALUES(2,'26-01-2020','Cortex')")
try:
    cursor.execute(query)
except Exception as error:
    print(error)
connection.close()
