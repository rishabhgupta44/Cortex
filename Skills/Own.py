# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

from Core.BrocaArea import create_learning_code, code_com, add_conv, sen_comp
from Core.Configure import auth
import os
import json
import string
import random


def response_checker(sen):
    with open('Brain/Limbic/JResponse/jresponse.json', 'r') as bg:
        frp = json.load(bg)
        fl = frp[1]['DATA']
        d_num = ''
        for vf in range(len(fl)):
            if sen.lower() == fl[vf]['R']:
                d_num = vf
        if isinstance(d_num, int):
            return 'PRESENT'


def del_sen_unex(sen_count):
    with open(
            os.path.join('Brain/FrontalLobe/understand/' +
                         'unexplained.json'), 'r') as reader_op:
        reader = json.load(reader_op)
        for y in range(len(reader)):
            if int(y) == int(sen_count):
                with open(
                        os.path.join('Brain/FrontalLobe/understand/' +
                                     'unexplained.json'), 'w+') as asdx:
                    del reader[y]
                    frop = json.dumps(bin)
                    asdx.write(reader)


def resc_hup():
    with open(
            os.path.join('Brain/FrontalLobe/understand/' +
                         'unexplained.json'), 'r') as sempu:
        crto = json.load(sempu)
        sko_count = ''
        stela = ''
        frpt = ''
        for vfro in range(len(crto)):
            cr_ar = crto[vfro]
            fra = cr_ar['Q']
            stela = input(fra + ' : ')
            if stela.lower() == 'y':
                sko_count = vfro
                dko = input('Learning code: ')
                dko = dko.upper()
                if dko == "" or dko == " ":
                    print("empty code")
                else:
                    cris = code_com(dko)
                    if cris == "CODE_NOT_PRESENT":
                        uro = input("In order to create code press (y/Y): ")
                        if uro == "" or uro == " ":
                            print("Response absent")
                        elif uro.lower() == "y":
                            df = auth()
                            qwd = input(
                                "In order to proceed you need to put your user access name: "
                            )
                            if df['USER_ACCESS_NAME'] == qwd.upper():
                                cl = input('Crate new learning code here:')
                                if cl == " " or cl == " ":
                                    print("Code absent")
                                else:
                                    create_learning_code(cl)
                                    frpt = dko
                            else:
                                print("unauthorised access")
                    else:
                        frpt = dko
                    frg = input("Sentence state level: ")
                    if frg == "" or frg == " ":
                        print("sen level not present")
                    else:
                        vrow = add_conv(fra, frg, frpt)
                        if vrow == "SEN_CREATED":
                            del_sen_unex(vfro)
            else:
                print("nothing")
        print(sko_count)
        '''with open(os.path.join('Brain/FrontalLobe/understand/'+'unexplained.json'),'w+') as asdx:
                del crto[sko_count]
                vfrps = json.dumps(crto)
                asdx.write(vfrps)'''


def g_create_r(code, level):
    with open(os.path.join('Brain/Response/' + 'response.json'),
              'r') as code_c:
        with open(
                os.path.join('Brain/FrontalLobe/understand/' +
                             'learning_code.json'), 'r') as code_collec:
            sec_code = json.load(code_c)
            vrc_code = json.load(code_collec)
            sen_g = ''
            sen_t = ''
            vrt = ''
            for den in range(len(sec_code)):
                sen_col_n = sec_code[den]
                sen_v_n = vrc_code[den]
                if sen_v_n == code:
                    grin = sen_col_n[sen_v_n]
                    if level == "high":
                        brp = grin[0]
                        vrt = brp['high']
                    elif level == "medium":
                        brp = grin[1]
                        vrt = brp['medium']
                    elif level == "low":
                        brp = grin[2]
                        vrt = brp['low']
                    with open('Brain/Limbic/JResponse/jresponse.json',
                              'r') as reader_j:
                        elic = json.load(reader_j)
                        crea = elic[1]['DATA']
                        n_vrt = vrt
                        gv = []
                        for v in range(len(crea)):
                            nf = crea[v]['R']
                            for hl in range(len(vrt)):
                                if nf == vrt[hl]:
                                    gv.append(nf)
                        for p in range(len(gv)):
                            vrt.remove(gv[p])
                        if len(vrt) == 0:
                            return 'RESPONSE_NOT_FOUND'
                        else:
                            grt = random.randrange(0, len(vrt))
                            if vrt[grt] == "A_G_OP":
                                print('hey')
                            else:
                                #create a checker for previous statements used
                                cv = response_checker(vrt[grt])
                                if cv == 'PRESENT':
                                    return vrt[grt]
                                else:
                                    return vrt[grt]


import documents

documents.NewEXEList()