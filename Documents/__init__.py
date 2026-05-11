# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import os,json,time
import BrocaArea as B

def NewEXEList():
        def EXEFileLister(path):
            try:
                z = B.FileHandler.__FileLogger__(path)
                for q in z[0]:
                    try:
                        FileList = os.listdir(q)
                        for t in FileList:
                            if os.path.isfile(q+'/'+t):
                                ExecCheck = t.split(".")
                                if ExecCheck[1] == "exe":
                                        time.sleep(0.1)
                                        print(q+t)

                    except:
                        pass
            except:
                    os.chmod(path,0)
                    NewDir = os.listdir(path)
                    print(f'\n\n\n{NewDir}\n\n\n')
                    for y in NewDir:
                        if os.path.isdir(path+'/'+y):
                           EXEFileLister(path+'/'+y)
        
        
        def specialCheck():
            OSCoolec = ["C:/Program Files/", "C:/Program Files (x86)/"]
            for x in OSCoolec:
                ListCollec = os.listdir(x)
                for y in ListCollec:
                    if os.path.isdir(x+'/'+y):
                        
                        try:
                            All = os.listdir(x+'/'+y)
                            print(All)   
                        
                        except:
                           
                            try:
                          
                                os.chmod(x+'/'+y,0)
                                All = os.listdir(x+'/'+y)
                          
                                for z in All:
                          
                                    if os.path.isfile(x+'/'+y+'/'+z):
                                        NewSlpit = z.split('.')
                          
                                        if NewSlpit[1] == "exe":
                                            print(x+'/'+y+'/'+z)
                          
                                    else:
                                        EXEFileLister(x+'/'+y+'/'+z)
                           
                            except:
                                pass
                    print(x,y)
        
        MainVolumes = ["C:","D:","E:","F:"]
        for x in MainVolumes:
                FirstShellDeepOs = os.listdir(x+'/')
                for y in FirstShellDeepOs:
                    if os.path.isdir(x+'/'+y):
                      if y !="$Recycle.BIN" and y != "$AVM":
                        try:
                            EXEFileLister(x+'/'+y)
                        except:
                                try:
                                    ErrorScan = os.listdir(x+'/'+y+'/')
                                    for c in ErrorScan:
                                        if os.path.isfile(x+'/'+y+'/'+c):
                                            ExecutionIndex = c.split('.')
                                            if ExecutionIndex == "exe":
                                                print(x+'/'+y+'/'+c)                                 
                                        elif os.path.isdir(x+'/'+y+'/'+c):
                                            EXEFileLister(x+'/'+y+'/'+c)
                                except:
                                    pass