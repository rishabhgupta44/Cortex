# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

#!/usr/bin/env python3

from reader import (Reader,auth,log)
from status import status
from jlist import listrecord
import datetime
import time
import calendar
#upload to .pacakge form
if '__main__' == __name__:
    import sys
    arg = sys.argv
    readr = Reader(1) #uses stage 1 for init file  
    options = ['upload','remove','status','packages']
    for x in arg:
        fur = 0
        #the action group
        if x[0] == '-':
            check = auth()
            if check == 1:
                log(f"jpm: auth[login] [{calendar.timegm(time.gmtime())}] [success]") 
                if x == '--upload' or x == '-u':
                    #upload takes file name for first then asks for the data
                    fur = arg.index(x)+1
                    readr.upload(arg[fur])
                if x == '--remove' or x == '-r':
                    #remove files 
                    fur = arg.index(x)+1
                    readr.remove(arg[fur])
            if check == 0:
                log(f"jpm: auth[login] [{calendar.timegm(time.gmtime())}] [fail]") 
                print("Wrong password")
        #the main function in jpm pacakge
        if x == 'status':
            execute = status()
            execute.execution()
        if x == 'packages':
            print("Package list: ")
            print()
            for x in listrecord():
                print(str(x)+'@jpm')

#Written for the Cortex archive