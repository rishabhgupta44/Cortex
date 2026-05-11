# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import datetime
import json
import os
import shutil
from datetime import date
from importlib import reload
import itertools
import threading
import time
import sys
import subprocess
import platform

from . import BrocaArea as bn
from Skills import Action as action
from . import BrocaArea as bronc
from SystemUtils import Tasks as tasks
#variables
pr_date = str(date.today())
cr_time = datetime.datetime.now()
month = cr_time.month
months = [
    "", "January", "Febuary", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
]
cr_month = months[month]
cr_year = str(cr_time.year)
directory = os.path.join('Brain/Limbic/' + cr_year + '/' + cr_month)
new_directory = os.path.join('Brain/Limbic/' + cr_year + '/' + cr_month)
u_directory = os.path.join('Brain/Limbic/User/' + cr_year + '/' + cr_month)
u_new_directory = os.path.join('Brain/Limbic/User/' + cr_year + '/' + cr_month)
cr_hour = cr_time.hour
#conditions
if not os.path.exists(directory):
    os.makedirs(directory)
    a = open(
        os.path.join('Brain/Limbic/' + cr_year + '/' + cr_month,
                     pr_date + '.txt'), 'a+')
    print("Sir, I have created a new folder")
else:
    a = open(
        os.path.join('Brain/Limbic/' + cr_year + '/' + cr_month,
                     pr_date + '.txt'), 'a+')
if not os.path.exists(u_directory):
    os.makedirs(u_directory)
    au = open(
        os.path.join('Brain/Limbic/User/' + cr_year + '/' + cr_month,
                     pr_date + '.txt'), 'a+')
    print("Sir, I have created a new folder for user")
else:
    au = open(
        os.path.join('Brain/Limbic/User/' + cr_year + '/' + cr_month,
                     pr_date + '.txt'), 'a+')
with open(os.path.join('Brain/Limbic/JResponse/' + 'jresponse.json'),
          'r') as res_j:
    fro = json.load(res_j)


#functions
def j_tem_cache():
    if (pr_date == fro[0]['CON_DATE']):
        return 'match'
    else:
        with open('Brain/Limbic/JResponse/jresponse.json', 'w+') as rf:
            fro[0]['CON_DATE'] = pr_date
            fro[1]['DATA'] = []
            vfx = json.dumps(fro)
            rf.write(vfx)
            return 'created'


def j_re_collector(sen):
    with open('Brain/Limbic/JResponse/jresponse.json', 'r') as rf:
        if sen != "":
            rpe = json.load(rf)
            gtp = rpe[1]['DATA']
            vfp = (gtp).append({'R': sen})
            with open('Brain/Limbic/JResponse/jresponse.json', 'w+') as rg:
                fnp = json.dumps(rpe)
                rg.write(fnp)


def j_re_reset():
    with open('Brain/Limbic/JResponse/jresponse.json', 'r') as rf:
        rpe = json.load(rf)
        rpe = [{'CON_DATE': ''}, {'DATA': ''}]
        with open('Brain/Limbic/JResponse/jresponse.json', 'w+') as rg:
            fnp = json.dumps(rpe)
            rg.write(fnp)


def registry(z, s):
    c = str(datetime.datetime.now())
    a.write(c + ' : ' + z + " " + "[ " + s + " ]" + "\n")
    au.write(c + ' : ' + z + "\n")
    rio = {'sentence': s}
    mrc = j_tem_cache()
    if mrc == 'match':
        j_re_collector(s)
    elif mrc == 'created':
        j_re_collector(s)


def greetings():
    if 0 <= cr_hour < 12:
        print("Good morning sir")
    if 12 < cr_hour < 16:
        print("Good afternoon sir")
    if 16 <= cr_hour <= 24:
        print("Good evening sir")


def listen(a):
    if a == "good":
        print("thanks")
    elif a == "bad":
        print("I apologize sir I will try to do my best next time ")
    elif a == "lol":
        print("he he he ")


def auth():
    with open(os.path.join('Brain/Limbic/sn/auth/' + 'u.json'),
              'r') as auth_op:
        auth_list = json.load(auth_op)
        return auth_list


def end(stat):
    stat = stat.lower()
    dn = bn.sen_t_code(stat)
    bronc.WSentence.Jauth('false')
    if dn[0] == 'CODE_GV_PRE':
        tasks.ThisSet('Cortex', 0)
        m = action.GetHistoryToLocalStorage()
        print('\x1b[32mcompleted')

        return 1


def timeTrig():
    utc_dt = datetime.datetime.now(datetime.timezone.utc)  # UTC time
    dt = utc_dt.astimezone()  # local time
    print(
        f'Sir the time is {dt.time().hour}:{dt.time().minute}:{dt.time().second}'
    )


def wifi(sen):
    if sen.lower() == 'connect to home network':
        os.system('netsh wlan connect TP-LINK_B142')
    if sen.lower() == 'connect to my mobile network':
        os.system('netsh wlan connect Redmi')


def clear_page():
    if platform.system() == 'Windows':
        os.system('start Main')
    else:
        # On Linux/Mac, clear screen instead
        os.system('clear' if platform.system() != 'Windows' else 'cls')


def nameDes():
    if shutil.which('figlet'):
        os.system('figlet Cortex')
    else:
        print('CORTEX')


def clear_scr():
    import platform
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')


def battery():
    print(f'Sir the device is running on electricity.')


def ping():
    os.system('ping "www.google.com"')


def correction(word):
    WordList = list(word)
    with open('Brain/FrontalLobe/words/all.json') as DicJSON:
        WordCollectionBasic = json.load(DicJSON)
        NameLength = len(word)
        for x in WordCollectionBasic:
            ArrayList = list(x)
            if int(NameLength) - 1 <= len(x) <= int(NameLength) + 1:
                if WordList[0] == x[0] and WordList[1] == x[1]:
                    print(x)


def ValueChecker(Number, List):
    # returns a list of maximum and minimum numbers init
    NumValue = True
    NumIndexMax = 0
    NumIndexMin = 0
    E1Arr = []
    E2Arr = []
    ValueNextNumber = 0
    if Number < min(List):
        return ["LIST_MIN_NOT_FOUND", min(List)]  # problem name , Max number
    if max(List) < Number:
        return ["LIST_MAX_NOT_FOUND", max(List)]  # problem name , Max number
    if Number == min(List):
        return ["CURRENT_MIN_VALUE", min(List)]  # problem name , Max number
    if max(List) == Number:
        return ["CURRENT_MAX_VALUE", max(List)]
    else:
        while NumValue:
            for x in List:
                if Number < x:
                    E1Arr.append(x)
                if x < Number:
                    E2Arr.append(x)
            NumValue = False
        return [min(E1Arr), max(E2Arr)]
