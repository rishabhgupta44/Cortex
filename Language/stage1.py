# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import os
import json
from . import _util
class SenceSniff():
    def __init__(self,sentence):
        self.sentence = sentence
        self.type = 'Neutral' #if the insertion continues then thier is a problem
        self.words = ' '
    def typeiden(self):
        '''
            The differenet type of sentences are :
                -> Declarative Sentence
                -> Imperative Sentence
                -> Exclamatory Sentence
                -> Interrogative Sentence
         =? Declarative sentence:
        '''
        pass