# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

#!usr/bin/env python3
import os
import json

'''

Most of the files I have are either json type or words so this module 
contains read and write function for each type

'''

15122019
JSON_FILES = {
                "RESPONSE": '/home/stark/Test/Brain/Response/response.json',
                "MEANING": '/home/stark/Test/Brain/FrontalLobe/meaning/meaning_o.json',
                "MEANINGS": '/home/stark/Test/Brain/FrontalLobe/meaning/word_meaning.json',
                "IDENTIFIER": '/home/stark/Test/Brain/FrontalLobe/understand/identifier.json',
                "LCODE": '/home/stark/Test/Brain/FrontalLobe/understand/learning_code.json',
                "UNDERSTAND": '/home/stark/Test/Brain/FrontalLobe/understand/understand.json',
                "UEXPLAINED": '/home/stark/Test/Brain/FrontalLobe/understand/unexplained.json',
                "WORDS": '/home/stark/Test/Brain/FrontalLobe/words/all.json',
                "WORD": '/home/stark/Test/Brain/FrontalLobe/words/words.json',
                "VERBS": "/home/stark/Test/Brain/FrontalLobe/words/verbs.json",
                "ADJECTIVE": "/home/stark/Test/Brain/FrontalLobe/words/adjective.json",
                "H": '/home/stark/Test/Brain/knowledge/hjson/h.json',
                "D": '/home/stark/Test/Brain/Limbic/JResponse/ADetails.json',
                "APPLICATION": '/home/stark/Test/Brain/Limbic/JResponse/application.json',
                "JRESPONSE": '/home/stark/Test/Brain/Limbic/JResponse/jresponse.json',
                "TSHELL": '/home/stark/Test/Brain/Limbic/JResponse/TShell.json',
                "APP": '/home/stark/Test/Brain/FrontalLobe/response/application/application.json',
                "WIFI": '/home/stark/Test/Brain/FrontalLobe/response/application/wi-fi.json',
                "AUTH": '/home/stark/Test/Brain/Limbic/sn/auth/auth_action.json',
                "CORTEX": '/home/stark/Test/Brain/Limbic/sn/auth/Cortex.json',
                "MAIN": '/home/stark/Test/Brain/Limbic/sn/auth/CortexMAIN.json',
                "USER": '/home/stark/Test/Brain/Limbic/sn/auth/u.json',
                "IDENTIFY": '/home/stark/Test/json/q.json',
                "ENGLISH":'/home/stark/Test/json/english.json',
                "IDENTITY":'/home/stark/Test/language/json/sentence.json'
             }


class _write(object):
    def __init__(
        self,
        code,
        type=None
    ):
        self.filecode = code
        print("class activated")


class _read(object):
    def __init__(
        self,
        returntype="",
    ):
        self.returntype = returntype

    def JSON(self, code):
        with open(JSON_FILES[code]) as file:
            if self.returntype.lower() == "array":
                return json.loads(file)
            else:
                return json.load(file)

    def TXT(self, name):
        with open(name) as file:
            return file.read()


#a test script to enduse or extract data from the os
'''
import sqlite3
db  = os.path.join('/home/stark/Test/','fuse.db')
DBConnection = sqlite3.connect(db)
CourS = DBConnection.cursor()
for s in arr:
    ConnectionExec = CourS.execute(f"INSERT INTO folder(place,type,os,use) VALUES('{s['PLACE']}','folder','linux','{s['NAME']}')")
DBConnection.commit()
if ConnectionExec:
   print("executed")
else:
    print("error")   
'''