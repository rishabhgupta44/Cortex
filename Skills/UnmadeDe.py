# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import json
import os
#type of sentence
def type_iden(sentence):
    st = sentence.lower().split()
    with open(os.path.join('Brain/FrontalLobe/understand/'+'identifier.json'),'r') as id_fr:
        iden_arr = json.load(id_fr)
        han_arr = iden_arr[0]
        han_id = han_arr['TYPE_CODE']
        for glick in range(len(han_id)):
            rampster = han_id[glick]
            fron = int(glick) + 1
            id_coll = iden_arr[fron]
            code_key_arr = id_coll[rampster]
            for urtp in range(len(code_key_arr)):
                if st[0] == code_key_arr[urtp]:
                         return rampster
def ty_c_t_us_c(sentence):
    frsp = type_iden(sentence)
    print(frsp)