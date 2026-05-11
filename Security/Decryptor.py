# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import json
import os
import random


def decryptor(encryptCode):
    encryptCode = encryptCode.split(encryptCode[0:3])[1]
    senAll = []
    file = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'

    with open(os.path.join(file + 'json/' + 'gap.json')) as gap_j:
        with open(os.path.join(file + 'json/' + 'encrypt.json')) as encr_j:
            encrypt_json = json.load(encr_j)
            gap_json = json.load(gap_j)
            for x in range(len(encrypt_json)):
                for y in gap_json:
                    if str(y) in str(encryptCode):
                        encryptCode = str(encryptCode).replace(str(y), ' ')

    senEn = encryptCode.split(' ')
    for z in senEn:
        for n in encrypt_json:
            if n['ENCRYPT'] == z:
                senAll.append(n['LETTER'])

    return ''.join(w for w in senAll)


def DoDecrypt(sen):
    return decryptor(decryptor(sen))
