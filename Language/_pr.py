#!usr/bin/env python3
# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import os
import json
#main code analyser that will brake down the code and tear the stuff into small fragments of data "chunks" of the sentences and reanalyze the data 

from ._util import _read, _write

# - Cortex archive
class SentenceInput(object):  #01072002
    def __init__(self, sentence):
        read = _read()
        self.words = sentence.lower().split(" ")
        self.verbs = read.JSON('VERBS')
        self.adjective = read.JSON('ADJECTIVE')
        self.UsedVerbs = []
        self.UsedAdjective = []
        self.UsedNoun = []
        self.UsedProNoun = []
        self.Object = []
        self.iscontinuous = False
        self.sentencetype = None 
        self.arrcon = []
        self.ContinuosDistruptor()
        self.VerbFinder()
        self.AdjectiveFinder()
    def ContinuosDistruptor(self):

        '''
    
        This function will remove the continuous "ing" from the sentence 
        which is mainly used as in future refrence and sence Cortex just 
        need to understand stuff it is nessasry to know the use of the 
        tense in it 
    
        '''
        for x in self.words:
            if "ing" in x: 
                self.words[self.words.index(x)] = x.split("ing")[0]
                self.iscontinuous = True
                self.arrcon.append(x)
        #returns the final marked points 
        #return self.words,self.iscontinuous, self.arrcon
        print(self.words,self.iscontinuous, self.arrcon)
    def VerbFinder(self):
        '''
           This function will just find the verbs used in the sentence and 
           later returns an array of the verb and the type of verb used in 
           the sentence
        '''
        self.ContinuosDistruptor()
        for x in self.verbs:
            if x['present'] in self.words: self.UsedVerbs.append({"word":x['present'],"type":"present"})
            if x['past'] in self.words: self.UsedVerbs.append({"word":x['past'],"type":"past"})
            if self.iscontinuous: pass
        print(self.UsedVerbs)
    def AdjectiveFinder(self):
        for x in self.adjective:
            if x in self.words:
                print(x)
