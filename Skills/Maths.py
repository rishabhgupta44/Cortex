# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

class Maths():
    def __init__(self,quiz):
        self.question = quiz
        self.identifier = ""
        self.init = 0
        self.result = 0
        self.more = []
        self.equal = 0
        self.before = 0
        print(self.question)

    def caller(self):
        if ("x") in self.question:
            self.equal = self.question.split("=")[1]
            self.before = self.question.split("=")[0]
            
            m = self.before.split("+")
            for k in m:
                if k != "x":
                   self.more.append(k)
                   self.identifier = "VARIABLE_TYPE"
            return( self.identifier,self.more,self.equal)

    def Classifier(self):
        self.caller()
        if self.identifier == 'VARIABLE_TYPE':
            self.result = int(self.equal)
            for a in self.more:
                self.result = self.result - int(a) 
        print(self.result)                                                                                                          

x = Maths("x+25+50=13")
x.Classifier()