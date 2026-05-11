# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

#!usr/bin/env python3
import os
import json
import sys
import time
import math

file = os.path.abspath(__file__).replace(os.path.basename(__file__),'')

def ultimate(number):
    r = list(number)
    bnum = 0
    for x in r:
        if x == '.':
            num = int(number.split('.')[0])
            bnum = int(number.split('.')[1])
            return((num*((10**len(number.split('.')[1])))+bnum)/10**len(number.split('.')[1]))             

def logreader():
    data = []
    #only pacakge info return
    with open(file+'.log/package.log','r') as log:
        lines = log.readlines()
    #for each lines
    for x in lines:
        init = {
            "action":" ",
            "timestamp": " ",
            "status": " ",
            "message":" "
        }
        Specarr = x.split(" ")
        #long bracket reader i.e spaces
        sentence = '' 
        arr = []
        for x in Specarr:
            if '[' in x:
                if ']' not in x:
                    for y in range(Specarr.index(x),len(Specarr)+1):
                        if ']' in Specarr[y]:
                            sentence = x+' '+Specarr[y] 
                            break
                    arr.append(sentence)
                if ']' in x:
                    arr.append(x)
        #action
        if '[' in arr[0]: 
            init['action'] = arr[0].split('[')[0]
            init['message'] = arr[0].split('[')[1].replace(']','')
        #timestamp
        init['timestamp'] = arr[1].replace('[','').replace(']','')
        #status successful/unsuccessful
        init['status'] = arr[2].replace('[','').replace(']','').replace('\n','')
            
        data.append(init)
    return data

class status(): 
    def data(self):
        self.init = logreader()
        return self.init
    def execution(self):
        self.data()
        last = self.init[len(self.init)-1]
        style = ''
        if last['status'] == 'success':
           style = '\x1b[32m'

        if last['status'] == 'fail':
           style = '\x1b[31m'
        print("Last Modified")
        print(f"  {time.ctime(math.floor(int(last['timestamp'])))} \x1b[1m {last['action']}\x1b[0m \x1b[34m{last['message']}\x1b[0m {style} {last['status']}\x1b[0m ")


#jpm manager 
#step 1. get details
# step 2. Set a plan
    