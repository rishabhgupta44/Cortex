# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

#!/usr/bin/env python3
import os
from subprocess import call

__version__ = '0.0.1'

class Modules(object):
    def __init__(
        self,
        module,
        location=""
        ):
        self.module = module
        self.location = location
        self.Class = []
        self.Functions = []
        self.IndependentFunction = []
        self.IndependentClass = []
        self.DirectImports = []
        self.FileLocation = ""
        try:
            self.File =  self.ReadData().split("\n")
            self.lines = len(self.File)
            self.ModuleReader()
            self.Imports()
        except:
            pass
    def ReadData(self):
        
        if not isinstance(self.module,str):
            print("ONLY MODULES ARE ALLOWED IN STRING")
        
        if isinstance(self.module,str):
            LinkFile = f'{str(self.module)}.py'
        
            if self.location != "":
                LinkFile = f'{self.location}/{str(self.module)}.py'
        
            if os.path.isfile(LinkFile):
                self.FileLocation = LinkFile
                #when module name is in string
                with open(LinkFile) as r:
                    return r.read()
                
            else:
                return ("LOCATION NOT FOUND")
    def ModuleReader(self):
        s1,j1 = ["",""]
        for x in self.File:
            if "def " in x:
               if "def" == x[0:3]:
                    s = x.split("def ")[1].split("(")[0]
                    self.Functions.append(s)
                    self.IndependentFunction.append(s)
               if " " in x[0] and " def " in x:
                    if "(" in x.split("def ")[1]:
                        j = x.split("def ")[1].split("(")[0]
                        self.Functions.append(j)
        
            if "class " in x:
                x1 = x.split(":")[0]
                if "class" == x1[0:5]:
                    
                        s1 = x1.split("class ")[1]
                        if "(" in s1:
                            s1 = s1.split("(")[0]
                        
                        self.Class.append(s1)
                        self.IndependentClass.append(s1)
            
                if " " in x[0] and " class " in x1 and '"' not in x1 and "'" not in x1:
                        j1 = x1.split("class ")[1]
                        if "(" in x1.split("class ")[1]:
                            j1 = j1.split("(")[0]
                        self.Class.append(j1)             
    def Imports(self):
        for y in self.File:
            if "import" == y[0:6]:
                Import  = y.split("import ")[1]
                if "as" in Import:
                    Import = Import.split(" as")[0]
                self.DirectImports.append(Import)
    def execute(self):
            call(["python3",self.FileLocation])
