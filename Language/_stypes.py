# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import os
import json


from _util import _read, _write
__version__ = '0.0.01'
28101982
'''
    This module consists of identifier functions and return the extracted 
    data from the sentence so that the computer will understand the real 
    meanaing of the question asked by the user
   
    sentence type = [I->interogative,A->conversationalist]

'''


class identifier(object):
    def __init__(self, sentence):
        read = _read()
        self.sentence = sentence.lower()
        self.words = sentence.split(" ")
        self.isabout = None
        self.SentenceType = True
        self.ispersonal = False
        self.useraccess = None
        self.identifyarray = read.JSON("IDENTIFY")
        self.sentencejson = read.JSON("IDENTITY")
        self.ParTypeSentence = []
        self.SentenceArray = {}
        self.structure = {
            "type": "",
            "word": "",
            "sense": ""
        }
        self._typeidentifier()
        self._about()
    def _tenseidentifier(self):
        pass
    def _typeidentifier(self):
        '''
            auxilary verbs -> [ is,are,was,were ]
            A sentence is mainly divided into three parts -> interogative,assimilative and i don't know the third one
        '''
        for x in self.sentencejson:
            for y in x['INIT']:
                if y.lower() in self.words:
                    if self.words.index(y.lower()) == 0:
                        print(x['TYPE'], y)
                        self.SentenceType = 'I'
                    if self.words.index(y.lower()) != 0:
                        if x['TYPE'] == 'AUXILLARY VERB':
                            self.structure['type'] = "AUX_VERB"
                            self.structure['word'] = y.lower()
                            print("appended", y)
                        if x['TYPE'] == 'QUESTION':
                            print("question", y)
                            self.ParTypeSentence.append("Q")
            print(self.structure)
        '''
           In the processing module the sortion of verbs will be done
        '''
    def _basicObejctFinder(self):
         self.GetRefinedObject = []
    def _about(self):
        for x in self.identifyarray[0]['PERSON']:
            for y in self.words:
                if y.upper() in x['ARGUMENT']:
                    print(x['TAG'], y)
