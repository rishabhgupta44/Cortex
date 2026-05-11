# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import sqlite3
import os

def listrecord():
    file = os.path.abspath(__file__).replace(os.path.basename(__file__),'')

    connect = sqlite3.connect(file+'.databases/packages.db')
    cur = connect.cursor()

    cur.execute("SELECT * FROM packages")

    mlist = cur.fetchall()
    flist = []
    for x in mlist:
        flist.append(x[1])
    
    return flist