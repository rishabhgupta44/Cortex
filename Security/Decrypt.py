# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import json
import os
import random

from . import Encryptor as Jencrypt

def decryptor(encryptCode):
     encryptCode = encryptCode.split(encryptCode[0:2])[1]
     senEn = ''
     senAll = []
     output = ''
     with open(os.path.join('json/'+'gap.json')) as gap_j:
        with open(os.path.join('json/'+'encrypt.json')) as encr_j:
          encrypt_json = json.load(encr_j)
          gap_json = json.load(gap_j)
          for x in range(len(encrypt_json)):
              for y in gap_json:
                  if str(y) in str(encryptCode):
                     encryptCode =  str(encryptCode).replace(str(y),' ')
     senEn = encryptCode.split(' ')      
     for z in senEn:
        for n in encrypt_json:
            if n['ENCRYPT'] == z:
                senAll.append(n['LETTER'])
     output = ''.join(w for w in senAll)
     return output
def DoDecrypt(sen):
    return decryptor(decryptor(sen))
print(DoDecrypt('_e.5579613458657410013557965234996914236611238865143365869814236586981424557961433996914009969140088981400557961400996914007676140086571400557961433661423661123768956144466112388651400768956142155796142155796142186571400889814108898143388651433865714249969143388651400557961421886514215579614216614006614217714108657144465869814237676143388981424658698112388981423996914105579614008657142176895614216586981421557961421767614149969144466142377144488651423661410661400661410865714449969144466141065869814005579614216586981410658698142386571423767614108865140099691421767614218657142155796142199691414889814338657142366112386571444771400865714149969141088981400996914337676142377112377144488981400768956141477140065869814148865143376761433767614247676143388981400886514148898140099691414865714238898112355796143388981423996914249969143388651444661444778865'))
