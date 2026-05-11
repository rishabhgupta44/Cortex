# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import datetime
import json
import os

from . import Configure

def DateModifier(date,datetype = str):
    if datetype == str:
        datesplit = date.split('-')
        return (datesplit[0],datesplit[1],datesplit[2])

class Cortex:
    def __init__(self):
        with open(os.path.join('Brain/Limbic/sn/auth/'+'cortex.json'),'r') as a_Cortex:
           Cortex = json.load(a_Cortex)
           self.age = Cortex['CREATION_DATE']
           self.datelist = DateModifier(self.age,str)
           self.version = Cortex['CORTEX_VERSION']
           self.creator = Cortex['C_NAME']        
           self.description = open('Brain/Limbic/sn/auth/'+'cortex.txt','r')
    def about(self):
            print('VERSION: '+ self.version+'\n'+'NAME: '+'CORTEX'+'\n'+'CREATORS NAME: '+self.creator+'\n'+'CREATION DATE: '+self.age)
            return ''
    def jDescription(self,n):
        if n == 1:
                Cortex = self.description.read()
                print((Cortex))
        if n == 2:
            print('My name is Cortex. I am an AI.')
    def jAger(self):    #debug the code 
        return "I don't know"
