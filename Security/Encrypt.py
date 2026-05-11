# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import json
import os
import random
from . import Decrypt


def encryptor(sen):
    sentence = list(sen)
    encrpytData = []
    xen = 'NOT_FOUND'
    with open(os.path.join('json/'+'encrypt.json')) as encr_j:
        with open(os.path.join('json/'+'gap.json')) as gap_j:
            encrypt_json = json.load(encr_j)
            gap_json = json.load(gap_j)
            for y in sentence:
                for x in encrypt_json:
                    if y == x['LETTER']:
                        encrpytData.append(x['ENCRYPT'])
    encrpyt = gap_json[random.randrange(0, len(gap_json))]+''.join(
        z+gap_json[random.randrange(0, len(gap_json))] for z in encrpytData)
    encrpyt = str(encrpyt)+str(gap_json[random.randrange(0, len(gap_json))])
    return '_e.'+encrpyt


print('\n')
sl = input('INPUT>')
Decrp = decryptor(sl)
print('\n') 
print(f'DECRYPTED>{Decrp}')

