# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

from . import JTasks
__Jtid__ = JTasks.__Jtid__
import json
import datetime
from . import Tasks as tasks
import os
class TasksHandler:
    def __init__(self):
        print("Hello world")
    def JTIDChecker():
        EmptyJTID = []
        if len(__Jtid__) == 0:
            return 1
        if sorted(__Jtid__,reverse=False) == list(range(1,max(__Jtid__)+1)):
            return max(__Jtid__)+1
        else:
            for x in list(range(1,max(__Jtid__)+1)):
                if not x in __Jtid__:
                    EmptyJTID.append(x)
            return EmptyJTID
def ThisSet(name,code):
    utc_dt = datetime.datetime.now(datetime.timezone.utc) # UTC time
    dt = utc_dt.astimezone() # local time
    timeNow = (f'{dt.time().hour}:{dt.time().minute}:{dt.time().second}')
    file = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
    MainApplicationJson = json.load(open(file+'Brain/Limbic/JResponse/application.json'))
    for x in MainApplicationJson:
        if x['TaskName'] == str(name):
           if int(code) == 0:
               x['ACTIVE'] = 'False'
               x['JTID'] = 0
               x['Time'] = timeNow
           if int(code) == 1:
               x['ACTIVE'] = 'True'
               x['Time'] = timeNow
               JTIDA = TasksHandler.JTIDChecker()
               if type(JTIDA) is list:
                    if len(JTIDA) !=0:         
                        #use the first possible value as th JTID
                        x['JTID'] = JTIDA[0]
               if type(JTIDA) is int:
                  x['JTID'] = JTIDA
    AnotherSept = json.dumps(MainApplicationJson)
    AnApp = open(file+'Brain/Limbic/JResponse/application.json','w')
    AnApp.write(AnotherSept)
