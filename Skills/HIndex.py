# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import win32com.client,pprint,ast,sys,os
import psutil
from pathlib import Path
arrTime = []
dataArr = []    
Arr1 = []
Arr2 = []
current_dir = Path('C:/Users/USER/AppData/Roaming/Microsoft/Windows/Recent/')
m = os.listdir(('C:/Users/USER/AppData/Roaming/Microsoft/Windows/Recent/'))
i=0
for path in current_dir.iterdir():
        Arr1.append({"Name":m[i],"Index":i})
        Arr2.append({"Time":path.stat().st_mtime,"Index":i})
        arrTime.append(path.stat().st_mtime)
        i+=1
arrTime.sort()
for x in arrTime:
    print(x)
#print(dataArr)
#print(arrTime[::-1])
#print(sys.argv)
#wmi=win32com.client.GetObject('winmgmts:')
#for p in wmi.InstancesOf('win32_process'):
#    print(p.Properties_('Name'))
    #process = psutil.Process(p.Properties_('ProcessId'))

    #process_name = process.name()
    #print(process_name)
    # (p.Name, p.Properties_('ProcessId'), \
    #    int(p.Properties_('UserModeTime').Value)+int(p.Properties_('KernelModeTime').Value))
    #if p.Name == "vlc.exe":
    #    print("vlc")
#    print(p.Name)
#    if p.Name == "vlc.exe":
#        print(pprint.saferepr(p))
        #children=wmi.ExecQuery('Select * from win32_process where ParentProcessId=%s' %p.Properties_('ProcessId'))
        #for child in children:
        #        print( '\t',child.Name,child.Properties_('ProcessId'), \
        #            int(child.Properties_('UserModeTime').Value)+int(child.Properties_('KernelModeTime').Value))

