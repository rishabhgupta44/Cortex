# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import os,string,json,time
import os
import string
import json
import time
from Core import BrocaArea as B

def oslist():
    MainVolumes = ["D:","E:","F:"]
    for x in MainVolumes:
        FirstShellDeepOs = os.listdir(x+'/')
        for y in FirstShellDeepOs:
           if os.path.isdir(x+'/'+y):
               if y != "$RECYCLE.BIN" and y != "$AVG":
                  try:
                    z = B.FileHandler.__FileLogger__(x+'/'+y)
                    for q in z[0]:
                        try:
                            FileList = os.listdir(q)
                            for t in FileList:
                                if os.path.isfile(q+'/'+t):
                                    time.sleep(0.1)
                                    print("\t\t\t"+t)

                        except:
                            pass
                  except:
                     pass
