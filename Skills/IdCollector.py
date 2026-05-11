# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import os, json
import Configure as config
from Utils import Decryptor as De
from Utils import Encryptor as Je
#COLLECT AND ADD DATA OF ALL THE UNAME AND PASSWORDS
#TRIPLE ENCRYPT THE DATA


def IDExecute():
    with open("json/idcollector.json", 'r') as ProCollection:
        return json.load(ProCollection)


def IDShell(Name, UName, Password):
    IDWCollect = IDExecute()
    IniTSHell = {
        "NAME": Je.encryptor(Name),
        "UNAME": Je.DoEncryptor(UName),
        "PASSWORD": Je.encryptor(Je.DoEncryptor(Password))
    }
    IDWCollect.append(IniTSHell)
    with open('json/idcollector.json', 'w+') as IDJsonWriter:
        Addidtion = json.dumps(IDWCollect)
        IDJsonWriter.write(Addidtion)
        return 1


def IDCollect():  #three step proccess
    inputIntake = input("USERNAME> ")
    AuthName = config.auth()
    IDExe = IDExecute()
    if inputIntake == De.DoDecrypt(AuthName['USER_ACCESS_NAME']):
        AppName = input('NAME> ')
        UserName = input('UNAME> ')
        Password = input('PASSWORD> ')
        ShellInput = IDShell(AppName, UserName, Password)
        print(ShellInput)


IDCollect()