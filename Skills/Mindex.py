# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import sqlite3,os,shutil
import pprint as ps
from pprint import pprint

#conn = sqlite3.connect('test.db')
#print ("Opened database successfully")

#cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
#for row in cursor:
#   print(row[0])
#print ("Operation done successfully")
#conn.close()


#path to user's history database (Chrome)
data_path = os.path.expanduser('~')+"/AppData/Local/Google/Chrome/User Data/Default"
files = os.listdir(data_path)

history_db = os.path.join(data_path, 'history')
#c = sqlite3.connect(history_db,timeout=60)
#m = c.cursor()
#v = m.execute("SELECT * FROM urls")
#for x in v:
#    print(x[0])
#querying the db
c = sqlite3.connect(history_db)
cursor = c.cursor()
m = cursor.execute("SELECT * FROM urls, visits WHERE urls.id = visits.url;")
results = cursor.fetchall() #tuple
m = ps.pformat(results)
print(m)
#for r in results:
#    print(r[0])
#    quit()