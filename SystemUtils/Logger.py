# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import datetime
import json
import os
import string

from Core import BrocaArea as Brain
from Security import Decryptor as De
from . import Tasks as tasks
from Core.Configure import auth
from Security.Decryptor import decryptor
from Security.Encryptor import encryptor

tasks.ThisSet('Logger', 1)
#Basic details of the date,time,month,directory, e.t.c

pr_date = str(datetime.date.today())
cr_time = datetime.datetime.now()
month = cr_time.month
months = [
    "", "January", "Febuary", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
]
cr_month = months[month]
cr_year = str(cr_time.year)
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
currentDirectory = os.path.join(root, f'Log/{cr_year}/{cr_month}')

file = root

#creating new directory if not exsists
if not os.path.exists(currentDirectory):
    os.mkdir(currentDirectory)
    directoryCreate = open(os.path.join(currentDirectory, pr_date + '.txt'),
                           'a+')


class Logger:
    def __LoggerWriteDirectory__(__content__):  #Logger writing directory
        if os.path.exists(currentDirectory):
            directoryCreate = open(
                os.path.join(currentDirectory, pr_date + '.txt'), 'a+')
            directoryActuator = open(
                os.path.join(currentDirectory, pr_date + '.txt'), 'w+')
            directoryActuator.write(__content__)
            return 'CREATED_1'

    def __LoggerReadDirectory__():  #logger reading function
        directoryCreate = open(
            os.path.join(currentDirectory, pr_date + '.txt'), 'a+')
        directoryActuator = open(
            os.path.join(currentDirectory, pr_date + '.txt'), 'r')
        return directoryActuator.read()

    def __content__(text):
        return encryptor(text)  #encrypting the content

    def __log__(text):  #main log function in the class to execute the log
        if text != '' or text != ' ':
            dir_read = Logger.__LoggerReadDirectory__()
            if dir_read != '':
                NewContent = f'{decryptor(dir_read)}\n{text}'
                Writer = Logger.__LoggerWriteDirectory__(
                    Logger.__content__(NewContent))
            if dir_read == '':
                Writer = Logger.__LoggerWriteDirectory__(
                    Logger.__content__(text))

    def __read__():
        try:
            UserNameList = auth()
            UserAuth = input('USERNAME> ')  #case sensitivity
            AuthJson = UserNameList['USER_ACCESS_NAME']  #auth json
            UserAuthName = De.DoDecrypt(AuthJson)
            if UserAuth == UserAuthName:  #user auth name
                IndexName = ''
                indexes = []
                DirArr = os.listdir('Log')
                for x in range(len(DirArr)):
                    print(f'{x+1}. {DirArr[x]}')
                try:
                    IndexInput = int(input('INPUT>'))
                    if int(IndexInput) <= len(DirArr):
                        NewDir = os.listdir(f'Log/{DirArr[IndexInput-1]}')
                        IndexName = f'Log/{DirArr[IndexInput-1]}'
                        for y in range(len(NewDir)):
                            print(f'{y+1}. {NewDir[y]}')
                        try:
                            Index = int(input('INPUT>'))
                            if Index <= len(NewDir):
                                DateList = (os.listdir(IndexName + '/' +
                                                       NewDir[int(Index) - 1]))
                                IndexName = IndexName + '/' + NewDir[int(Index)
                                                                     - 1] + '/'
                                for z in range(len(DateList)):
                                    print(
                                        f'{z+1}. {str(DateList[z]).replace(".txt","")}'
                                    )
                                try:
                                    FileIndex = int(input('INPUT>'))
                                    if FileIndex <= len(DateList):
                                        File = open(IndexName +
                                                    DateList[int(FileIndex) -
                                                             1])
                                        print(decryptor(File.read()))
                                except:
                                    print('Error')
                        except:
                            print('Error')
                except:
                    print('Error')
        except:
            print('Error')


ReadJson = json.load(open(file + 'Brain/Limbic/JResponse/TShell.json'))
if ReadJson['Log'] == 'WRITE':

    LogInput = input('LOG>')
    Logger.__log__(LogInput)
    ReadJson['Log'] = ''
    newJson = json.dumps(ReadJson)
    JsonWrite = open(file + 'Brain/Limbic/JResponse/TShell.json', 'w')
    JsonWrite.write(newJson)
    tasks.ThisSet('Logger', 0)

if ReadJson['Log'] == 'READ':

    if __name__ == '__main__':

        while True:

            Logger.__read__()
            takeIn = input()
            if takeIn == '':
                ReadJson['Log'] = ''
                newJson = json.dumps(ReadJson)
                JsonWrite = open(file + 'Brain/Limbic/JResponse/TShell.json',
                                 'w')
                JsonWrite.write(newJson)
                tasks.ThisSet('Logger', 0)
                break
