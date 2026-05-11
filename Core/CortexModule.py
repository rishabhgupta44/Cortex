# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------
from .Configure import listen, registry, greetings, auth, j_tem_cache, j_re_reset, end, timeTrig, wifi, clear_page, clear_scr
from . import BrocaArea as B
from .Response import JResponse, g_create_r, remp_fric, sen_punc_differ, sym_find, resc_hup, response_crea
import string
import os
import json
import sys
import subprocess
import platform
from Skills import Action as action
from SystemUtils import Tasks as tasks

# Try to import pyautogui, but don't fail if X11 display is not available
try:
    import pyautogui
except Exception:
    pyautogui = None

from importlib import reload
from Skills import Action as action
import CodeReac as cdrec
from Security import Decryptor as De
   
def Cortex():
    
    stat = input('CORTEX>').lower()
    
    wifi(stat)
    vro = B.ESentence.SentenceTC(stat)
    cdrec.code_rep(vro[0])
    action.SearchAbout(stat)
    vp = ''
    
    if vro == 'X':
        B.WSentence.UndefinedSen(stat)
    
    else:
        if vro[0] == "CODE_MEA_QUE_PRI":
            remp_fric(stat)
        B.WSentence.UndefinedSen(stat)
        if sym_find(stat) == True:
            sen_punc_differ(stat)
        else:
            vp = g_create_r(vro[0], vro[1])
        cdrec.ResponseRefiner(stat, vp)
    
    if stat.upper() == "CODE_SEN":
        JResponse.CResponse()
        vp = ''
    
    if 'about jtask' in stat:
        Nsentence = stat.split('about jtask ')
        TJReader = json.load(open('Brain/Limbic/JResponse/TShell.json'))
        TJReader["TaskName"] = Nsentence[1]
        TFinal = json.dumps(TJReader)
        TJWriter = open('Brain/Limbic/JResponse/TShell.json', 'w')
        TJWriter.write(TFinal)
        # Cross-platform: Open TDetail.py
        if platform.system() == 'Windows':
            os.system('start TDetail.py')
        else:
            subprocess.Popen([sys.executable, 'TDetail.py'])
    
    if 'install python library' in stat:
        mr = stat.split('install python library ')
        os.system(f'pip install {mr[1]}')
    
    if stat == "new learning code":
        df = auth()
        frp = input(
            "In order to proceed you need to put your user access name: ")
        mn = De.DoDecrypt(df['USER_ACCESS_NAME'])
        if mn.upper() == frp.upper():
            cl = input('Crate new learning code here:')
            B.WSentence.CreateLC(cl)

        else:
            print("unauthorised access")

    mer = end(stat)

    if mer == 1:
        tasks.ThisSet('PendriveBackup', 0)
        j_re_reset()       
        return 1
