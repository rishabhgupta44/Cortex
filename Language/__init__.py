# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

#!usr/bin/env python3
#This script is written for the Cortex archive
import json
import os
import sys
import _stypes as _s

from _util import (_read,_write)

'''

    Language processing area for Cortex

    This package consists of language synthesizer and some trainig modules 
    which will help Cortex to understand the use of words in a sentences 
    correctly. Cortex will also record all the user input for future 
    refrences but it is only accessable by the alpha user and may be after 
    some time Cortex will be able to speak by himself 

                          NOTE

                 Later used in broca_area
'''
__version__='0.0.01' 
OPEN = open
15122019,12091978

import _stypes, _pr

class _Parser(object):
    def __init__(self,sentence):
        self.sentence = sentence
        self.s1 = _stypes.identifier(self.sentence)
        self.s2 = _pr.SentenceInput(self.sentence)
_Parser("Hey Cortex can you help me with this")
