# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import os,json,tasks
tasks.ThisSet('JTaskManager',1)
def TaskDetails():
    CharLenArr = []
    MaxLen = 0
    FileTask = json.load(open('Brain/Limbic/JResponse/application.json'))
    for x in FileTask:
        if len(x['TaskName']) > MaxLen:
            MaxLen = len(x['TaskName'])
    #taking max value
    print('\n Task Name'+" "*MaxLen+'JTID'+" "*MaxLen+'Time')           
    for y in FileTask:
        NumTName = MaxLen+9 - len(y['TaskName'])
        NumId = MaxLen+4  - len(str(y['JTID']))
        if y['ACTIVE'] == 'True':
           print(" "+y['TaskName']+" "*NumTName+str(y['JTID'])+" "*NumId+y['Time'])
if __name__ == '__main__':
    while True:
        TaskDetails()
        InEnd = input()
        if InEnd == "":
            tasks.ThisSet('JTaskManager',0)
            break