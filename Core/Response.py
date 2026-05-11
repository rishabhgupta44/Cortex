# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

from .BrocaArea import sen_t_code, meaning, add_conv, code_com, create_learning_code
from .Configure import greetings, auth
import string
import os
import json
import random
from Security import Decryptor as De
from . import BrocaArea as Brain
def response_checker(sen):
    with open('Brain/Limbic/JResponse/jresponse.json','r') as bg:
         frp = json.load(bg)
         fl = frp[1]['DATA']
         d_num = ''
         for vf in range(len(fl)):
            if sen.lower() == fl[vf]['R']:
                d_num = vf
         if isinstance(d_num,int):
            return 'PRESENT'          
def g_create_r(code,level):
    with open(os.path.join('Brain/Response/'+'response.json'),'r') as code_c:
        with open(os.path.join('Brain/FrontalLobe/understand/'+'learning_code.json'),'r') as code_collec:
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
                    with open('Brain/Limbic/JResponse/jresponse.json','r') as reader_j:
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
                         if len(vrt) == 0 :
                            return 'RESPONSE_NOT_FOUND'
                         else: 
                            grt = random.randrange(0,len(vrt))
                            if vrt[grt] ==  "A_G_OP":
                                greetings()
                                return 'GREETINGS'
                            else:    
                            #create a checker for previous statements used
                                cv = response_checker(vrt[grt])
                                if cv == 'PRESENT':
                                    return vrt[grt]
                                else:
                                    return vrt[grt]
def remp_fric(sentence):
    drim = sen_t_code(sentence)

    if drim[0] == "CODE_MEA_QUE_PRI":
        with open(os.path.join('Brain/FrontalLobe/understand/'+'understand.json'),'r') as remp:
            with open(os.path.join('Brain/FrontalLobe/understand/'+'learning_code.json'),'r') as rict:
                crip = json.load(remp)
                fto = json.load(rict)
                cro_count = ''
                for vict in range(len(crip)):
                    vcin = crip[vict]
                    closs = vcin[fto[vict]]
                    for kriv in range(len(closs)):
                        envic = closs[kriv]
                        if envic['sentence'] in sentence:
                            cro_count = [vict,kriv]
            sem = crip[cro_count[0]]
            sro = fto[cro_count[0]]
            drick = sem[sro]
            driv = drick[cro_count[1]]
            mrip = driv['sentence']

            semdp = sentence.lower().split(mrip+' ')
            meaning(semdp[1])
def sym_find(sen):
    dro = [',','and']
    drp = ''
    for das in range(len(dro)):
        if dro[das] in sen:
            drp = das
    if(isinstance(drp,int)):
        return True
    else:
        return False
def sen_punc_differ(sentence):
    vrtp = []
    csxp = [',','and']
    for vrx in range(len(csxp)):
        if csxp[vrx] in sentence:
            vrtp = sentence.split(csxp[vrx])
    brmp = (vrtp[0]).replace(" ","")
    secp = sen_t_code(brmp)
    if secp[0] == "CODE_MEET_PRI":
        vfrp = (vrtp[1]).strip()
        brox = sen_t_code(vfrp)
        g_create_r(brox[0],brox[1])
def resc_hup():
    with open(os.path.join('Brain/FrontalLobe/understand/'+'unexplained.json'),'r') as sempu:
            crto = json.load(sempu)
            sko_count = ''
            stela = ''
            frpt = ''
            fra = ''
            for vfro in crto:
                fra = vfro['Q']
                stela = input(f'- {fra} :')
                if stela.lower() == 'y':
                    sko_count = crto.index(vfro)
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
                                qwd = input("In order to proceed you need to put your user access name: ")
                                if De.DoDecrypt(df['USER_ACCESS_NAME']) == str(qwd.upper()):
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
                        if frg =="" or frg ==" ":
                            print("sen level not present")
                        else:
                            vrow = add_conv(fra,frg,frpt)
                            if vrow == "SEN_CREATED":
                                    sko_count = vfro
                else:
                    print("nothing")                
            with open(os.path.join('Brain/FrontalLobe/understand/'+'unexplained.json'),'w+') as asdx:
                if sko_count == '':
                    print("Aborted")
                else:
                    del crto[sko_count]
                    vfrps = json.dumps(crto)
                    asdx.write(vfrps)
def response_crea(code,lev,resp):
    code = code.upper()
    lev = lev.lower()
    resp = resp.lower()
    with open('Brain/Response/'+'response.json') as rep:
      with open('Brain/FrontalLobe/understand/'+'learning_code.json') as lr_c:
            new_rep = json.load(rep)
            lrc = json.load(lr_c)
            cou_a = ''
            for a in range(len(new_rep)):
                if code == lrc[a]:
                    cou_a = a
            if isinstance(cou_a,int):
               #print(new_rep[cou_a][lrc[cou_a]]) 
               grf = ''
               if lev == 'high':
                   grf = new_rep[cou_a][lrc[cou_a]][0]['high']
               if lev == 'medium':
                   grf = new_rep[cou_a][lrc[cou_a]][1]['medium']
               if lev == 'low':
                   grf = new_rep[cou_a][lrc[cou_a]][2]['low']
               if grf == '':
                   print('level not found')
               else:
                   #response [present checker]
                   fg = 0
                   for x in range(len(grf)):
                       if grf[x] in resp:
                           fg = 1
                   if fg == 0:
                        grf.append(resp)
                        with open('Brain/Response/'+'response.json','w+') as op:
                            fre = json.dumps(new_rep)
                            op.write(fre)
                            return 'CREATED'
                   elif fg == 1:
                       print('present in the sentence')
            else:
                print("CODE_NOT_FOUND")

class JResponse:
   def CResponse():
        '''
          Create or delete Response in Cortex module
        '''
        import getpass
        UserAuth = getpass.getpass('USERNAME> ')    #case sensitivity
        AuthJson = Brain.FileHandler.FileJsonResp('FILE_AUTH')  #auth json
        UserAuthName = De.DoDecrypt(AuthJson['USER_ACCESS_NAME'])
        if UserAuth == UserAuthName:   #user auth name
           
           UnexplainedJson = Brain.FileHandler.FileJsonResp('FILE_UNEXPLAINED')
           for x in UnexplainedJson:
               UnexplainedQuestion = input('RESPONSE>'+x['Q']+': ')  #Response taker
               if UnexplainedQuestion.lower() == 'y':
                  UnexplainedCodeQuestion = input('CODE> ').upper()
                  CodeCheck = Brain.CSentence.codeCheck(UnexplainedCodeQuestion)

                  if CodeCheck[0] == 'CODE_N_PRESENT':   #if code is not present make code
                        if UnexplainedCodeQuestion != '':
                            CheckQuery = input('CONFORMATION> ')
                            if CheckQuery.lower() == 'y':
                            
                                Brain.WSentence.CreateLC(UnexplainedCodeQuestion)
                            if CheckQuery.lower() != 'y':
                                UnexplainedCodeQuestion = ''       
                        if UnexplainedCodeQuestion == '':
                                UnexplainedCodeQuestion = ''       

                  if UnexplainedCodeQuestion != '':     #if it is empty
                            
                            UnexplainedLevelQuestion = input('LEVEL> ')
                            
                            if UnexplainedLevelQuestion != '':
                            
                                Brain.WSentence.CreateSen(UnexplainedCodeQuestion, x['Q'], UnexplainedLevelQuestion)
                                UnexplainedJson.remove(x)
                                Brain.FileHandler.FileJsonWri('FILE_UNEXPLAINED',UnexplainedJson)
                    
               if UnexplainedQuestion.lower() == 'delete':
                  UnexplainedJson.remove(x)
                  Brain.FileHandler.FileJsonWri('FILE_UNEXPLAINED',UnexplainedJson)

# i have to create a new module for speak function for Cortex
