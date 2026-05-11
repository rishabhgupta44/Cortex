# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import os,json,string
k = input('> ').lower()
def first_word_type(sen):
    #first word
    fro = sen.split(" ")
    main = fro[0]
    with open(os.path.join('Brain/FrontalLobe/understand/'+'identifier.json')) as inType:
         idCollector = json.load(inType)
         idFirstCollector = idCollector[0]['TYPE_CODE']
         i = 0
         try:
            for x in range(len(idCollector)):
                fros = idCollector[0]['TYPE_CODE']
                i+=1    
                cv = fros[i-1]
                if i<= len(idCollector):
                    wordColl = idCollector[i][cv]
                    for y in wordColl:
                        if main == y:
                            print(idFirstCollector[i-1])
         except:
             return 2
first_word_type(k)
