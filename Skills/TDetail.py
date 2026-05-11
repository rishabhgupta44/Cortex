# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import os, json, tasks
tasks.ThisSet('JTDetail', 1)
TName = json.load(open('Brain/Limbic/JResponse/TShell.json'))
#some file import
print(' Press Enter to exit...')
FileTask = json.load(open('Brain/Limbic/JResponse/application.json'))
TaskDetail = json.load(open('Brain/Limbic/JResponse/ADetails.json'))
for x in FileTask:
    for y in TaskDetail:
        if TName['TaskName'] == y['TaskName'].lower() == x['TaskName'].lower():
            print(
                f"\n Name: {y['TaskName']}\n Detail: {y['Detial']}\n Type: {y['PType']}\n Version: {y['Version']}\n Priority: {y['Priority']}\n Active: {x['ACTIVE']}\n JTID: {x['JTID']}\n Time: {x['Time']}\n"
            )

if __name__ == '__main__':
    while True:
        Ending = input()
        if Ending == '':
            TJReader = json.load(open('Brain/Limbic/JResponse/TShell.json'))
            TJReader["TaskName"] = ""
            TFinal = json.dumps(TJReader)
            TJWriter = open('Brain/Limbic/JResponse/TShell.json', 'w')
            TJWriter.write(TFinal)
            tasks.ThisSet('JTDetail', 0)
            break