# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import datetime
import json
import os
import string

# Try to import pyautogui, but don't fail if X11 display is not available
try:
    import pyautogui
except Exception:
    pyautogui = None

from Skills import Action as action
from Core import BrocaArea as B
from Core import Configure as config
from Security import Decryptor as De
from SystemUtils import Refresh as Re
from SystemUtils import Tasks as tasks
from Skills import DocumentLister as Doc
from subprocess import call as _
from Core.CortexSelf import Cortex
from Core.Response import (JResponse, g_create_r, remp_fric, resc_hup,
                      response_crea, sen_punc_differ, sym_find)


def code_rep(code):
    code = code.upper()
    if code == 'CORTEX_CREATION_DETAIL':
        Cortex.creation('CORTEX_CREATION')
    if code == 'CORTEX_CREATOR_DETAIL':
        Cortex.creation('CORTEX_CREATOR')
    if code == 'CODE_TIME_N':
        time = datetime.datetime.now()
        now = time.time()
        print(now)
    if code == 'CODE_SEN':
        resc_hup()
    if code == 'CODE_ACT_ASK_PRI':
        print('As being latest version to my pria For now i can just learn things')


def ResponseRefiner(sentence, response):
    vp = response
    if vp == 'BATTERY_STAT':
        config.battery()
        vp = ''
    if vp == 'CREATOR_NAME':
        print('I was created for the Cortex archive')
        vp = ''
    if vp == 'RESPONSE_NOT_FOUND':
        print("CORTEX>I think you have repeated the question many time")
        vp = ''
    if vp == 'SEARCH_PRI_ACTION':
        dsf = action.searchAppSpec(sentence)
        if dsf == 1:
            print('starting sir...')
            vp = ''
    if vp == 'TIME_TRIG':
        config.timeTrig()
        vp = ''
    if vp == 'CODE_APPLICATION_START':
        action.searchAppSpec(sentence)
        action.acOpner(sentence)
        vp = ''
    if vp == 'LOGGER_PRE':
        ReadJson = json.load(
            open('/home/stark/Test/Brain/Limbic/JResponse/TShell.json'))
        ReadJson['Log'] = 'WRITE'
        newJson = json.dumps(ReadJson)
        JsonWrite = open('/home/stark/Test/Brain/Limbic/JResponse/TShell.json', 'w')
        JsonWrite.write(newJson)
        _(['python3','Logger.py'])
        vp = ''
    if vp == 'VERSION_PLATE':
        _(['python3','Version.py'])
        vp = ''
    if vp == 'BORN_AGE':
        J = Cortex()
        print(J.jAger())
        vp = ''
    if vp == 'CREATION_DATE':
        Bdate = "I was created on 17th July,2019"
        print(Bdate)
        vp = ''
    if vp == 'BORN_DATE':
        Bdate = "I was born on 17th July,2019"
        print(Bdate)
        vp = ''
    if vp == 'CLEAR_SCREEN':
        config.clear_scr()
        vp = ''
    if vp == 'SELF_DESCRIBE':
        J = Cortex()
        J.jDescription(1)
        vp = ''
    if vp == 'NAME_DESCRIBE':
        J = Cortex()
        J.jDescription(2)
        vp = ''
    if vp == 'BACKUP_PANNEL':
        B.FileHandler.FileBackup()
        vp = ''
    if vp == 'REFRESH_PANNEL':
        Re.refresh()
        print('CORTEX>Pannel refreshed')
        vp = ''
    if vp == 'CHECK_PING':
        config.ping()
        vp = ''
    if vp == 'LOG_READ':
        ReadJson = json.load(
            open('/home/stark/Test/Brain/Limbic/JResponse/TShell.json'))
        ReadJson['Log'] = 'READ'
        newJson = json.dumps(ReadJson)
        JsonWrite = open('/home/stark/Test/Brain/Limbic/JResponse/TShell.json', 'w')
        JsonWrite.write(newJson)
        _(['python3','Logger.py'])
        vp = ''
    if vp == 'VIDEO_HISTORY':
        action.ApUse()
        vp = ''
    if vp == 'MOVIE_PLAY':
        Doc.PlayMovie(sentence)
        vp = ''
    else:
        config.registry(sentence, vp)
        if vp != '':
            print(vp)
