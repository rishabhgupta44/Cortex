# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

#!/usr/bin/env python3
import os
import json
from Skills import Text as text
import time

__inactive__ = []
__Jtid__ = []
i=0

while i==0:
    ApplicationJson = json.load(open('Brain/Limbic/JResponse/application.json'))
    for x in range(len(ApplicationJson)):
        if ApplicationJson[x]['ACTIVE'] == 'False':
            __inactive__.append(ApplicationJson[x]['TaskName'])
        if ApplicationJson[x]['ACTIVE'] == 'True':
            __Jtid__.append(ApplicationJson[x]['JTID'])
    i=1
__inactive__
__Jtid__

def init(save):
    var = str(save)
    aggr = ["a","v","m"]
    for x in var:
        for y in aggr:
            if x == y:
               return 1
            if x!= y:
               return 0 

nem = init("Data type")

__jh__=0
