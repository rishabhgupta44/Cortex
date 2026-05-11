# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import doctest
import json
import os
import pathlib
import time
from pathlib import Path


from Core import BrocaArea as B
from Core import Configure as config

# basic program which has every file name and details in this pc
extensions = ['png', 'img', 'jpg', 'jpeg', 'pdf', 'doc', 'docx']


def FolderNameSet(name):
    if " " in name:
        print('space present')
# I have mainly three slots C: D: E: F: Cortex has no authorisation to get in C: but it can take the rest of the files
def VolumeFolderPath():
    AllFileVolumes = ["D:", "E:", "F:"]
    AllVolumeFiles = []
    MainReturnsFilePath = []
    MainReturnsFileName = []
    for x in AllFileVolumes:
        dir = os.listdir(x+'/')
        CollectionVolumeName = [x, dir]
        AllVolumeFiles.append(CollectionVolumeName)
        #AllFiles = B.FileHandler.__FileLogger__(x+'/')
    for y in AllVolumeFiles:
        for z in y[1]:
            if os.path.isdir(y[0]+'/'+z):
                try:
                    MainReturnsFilePath.append(
                        B.FileHandler.__FileLogger__(y[0]+'/'+z)[0])
                except:
                    pass
    return MainReturnsFilePath
def VolumeFolderName():
    AllFileVolumes = ["D:", "E:", "F:"]
    AllVolumeFiles = []
    MainReturnsFileName = []
    for x in AllFileVolumes:
        dir = os.listdir(x+'/')
        CollectionVolumeName = [x, dir]
        AllVolumeFiles.append(CollectionVolumeName)
        #AllFiles = B.FileHandler.__FileLogger__(x+'/')
    for y in AllVolumeFiles:
        for z in y[1]:
            if os.path.isdir(y[0]+'/'+z):
                try:
                    MainReturnsFileName.append(
                        B.FileHandler.__FileLogger__(y[0]+'/'+z)[1])
                except:
                    pass
    return MainReturnsFileName
def DocumentJSONAdder(FileName):
    VolumePaths = VolumeFolderPath()
    OSAllNameArr = []
    VolumeName = VolumeFolderName()
    for x in range(len(VolumePaths)):
        for y in range(len(VolumePaths[x])):
            with open('json/'+FileName, 'a+') as JsonWRiters:
                try:
                    JsonWRiters.write(
                        '{'+'"'+"PATH"+'"'+":"+'"'+VolumePaths[x][y]+'"'+'}'+','+'\n')
                    print("Success")
                except:
                    print("fail")
def VolumeFilesContainer():
    AllFileVolumes = ["D:", "E:", "F:"]
    AllVolumeFiles = []
    MainReturnsFilePath = []
    MainPaths = []
    MainReturnsFileName = []
    for x in AllFileVolumes:
        dir = os.listdir(x+'/')
        for y in dir:
            try:
                if os.path.isdir(x+'/'+y):
                    NewDirectories = os.listdir(x+'/'+y+'/')
                    for z in NewDirectories:
                        if os.path.isfile(x+'/'+y+'/'+z):
                            with open('json/FileNameList.json', 'a+') as JsonWRite:
                                JsonWRite.write('{'+'"'+"FILENAME"+'"'+":"+'"'+z+'"'+','+'"'+"PATH"+'"'+':'+'"' +
                                                x+'/'+y+'/'+'"'+','+'"'+'EXECUTABLE'+'"'+':'+'"'+x+'/'+y+'/'+z+'"'+'}'+','+'\n')
                                print(x+'/'+y)
                                print("Success")
                #NewWholeDir = os.listdir(x+'/'+y+'/')
                # print(y)
                # with open('json/FileHeadList.txt','a+') as JsonWRite:
                #         JsonWRite.write('{'+'"'+"FILENAME"+'"'+":"+'"'+y+'"'+','+'"'+"PATH"+'"'+':'+'"'+x['PATH']+'"'+','+'"'+'EXECUTABLE'+'"'+':'+'"'+x['PATH']+'/'+y+'"'+'}'+','+'\n')
            except:
                print("Fail")
        AllVolumeFiles.append(dir)
def AllFileDefination():
    with open('json/FolderLists.json') as FolderCollection:
        Folder = json.load(FolderCollection)
        for x in Folder:
            try:
                FileName = os.listdir(x['PATH'])
                for y in FileName:
                    if os.path.isfile(x['PATH']+'/'+y):
                        with open('json/FileNameList.json', 'a+') as JsonWRite:
                            JsonWRite.write('{'+'"'+"FILENAME"+'"'+":"+'"'+y+'"'+','+'"'+"PATH"+'"'+':'+'"' +
                                            x['PATH']+'"'+','+'"'+'EXECUTABLE'+'"'+':'+'"'+x['PATH']+'/'+y+'"'+'}'+','+'\n')
                            print("Success")
            except:
                print("Fail")
def deepAnalyzer(word):
    pass
'''
def BruteForceSearch(Word, extension):
    if extension == '.docx':
        SearchFileType = __SearchLogger__.FolderSearch('.docx')
        WordFile = ""
        try:
            for x in SearchFileType:
                OpenFiles = docx2txt.process(x)
                if Word.lower() in OpenFiles.lower():
                    print(x)
                time.sleep(2)
        except:
            print("Fail")

    if extension == '.txt':
        SearchFileType = __SearchLogger__.FolderSearch('.txt')
        WordFile = ""
        for x in SearchFileType:
            try:
                with open(x, 'r') as ReadFile:
                    ReadFileContent = ReadFile.read()
                    if Word.lower() in ReadFile.read().lower():
                        print(x)
                        time.sleep(5)
            except:
                with open(x, 'rb') as ReadFile:
                    ReadFileContent = ReadFile.read()
                    if Word in ReadFile.read():
                        print(x)
                        time.sleep(5)
'''
def SpecFileListner(FileName, SpecName):
    ResultArr = []
    with open(FileName) as ma:
        ReadLines = ma.readlines()
        IntDex = 0
        ElementArr = []
        ElementArrFDef = []
        for x in ReadLines:
            ElementIndex = ReadLines.index(x)
            IntIndex = int(ElementIndex)-1
            if SpecName == 'class':
                if SpecName.lower() in x.lower():
                    NewElement = (x).split(SpecName.lower())
                    if NewElement[0] == '':
                        if ':' in NewElement[1]:
                            NewWord = NewElement[1].split(':')
                            ElementArr.append([NewWord[0], ReadLines.index(x)+1])
            if SpecName == 'def':
                ClassExtin = SpecFileListner(FileName, 'class')
                if 'def ' in x.lower():
                    NewElement = (x).split('(')
                    DefSeprator = NewElement[0].split("def ")
                    if DefSeprator[0] != "":
                        CurrentDefIndex = ReadLines.index(x)+1
                        ErArr = []
                        for y in ClassExtin:
                            ErArr.append(y[1])
                        Max_Min = config.ValueChecker(CurrentDefIndex, ErArr)
                        for z in ClassExtin:
                            if z[1] == Max_Min[1]:
                                ResultArr.append(
                                    ["CLASS_DEF", z[0], DefSeprator[1]])
                    if DefSeprator[0] == "":
                        ResultArr.append(["NO_CLASS_DEF", DefSeprator[1]])
        if SpecName == 'class':
            return ElementArr
        if SpecName == 'def':
            return ResultArr
def JarvisListerSearch():
    allPyFile = os.listdir('.')
    for x in allPyFile:
        if os.path.splitext(x)[1] == '.py':
            if x != 'DocumentLister.py':
                AllDef = SpecFileListner(x, 'def')
                print(AllDef)
def PlayMovie(sentence):
    m = __SearchLogger__(True, "movie")
    with open(os.path.join('Brain/FrontalLobe/understand/'+'understand.json')) as inload:
        jsonload = json.load(inload)
        SpecSent = jsonload[24]["MOVIE_PLAY"]
        for y in SpecSent:
            if y["sentence"] in sentence:
                name = sentence.split(y["sentence"]+' ')[1]
        zs = m.FileSearch(name)
        for x in (zs[1]):
            confirm = input(f'Do you want me to play {x} [y/n]: ')
            if confirm.lower() == 'y':
                os.startfile(zs[0][zs[1].index(x)])
                print(f"playing {name}...")
                break
                
#class to search for documents
class __SearchLogger__:
    def __init__(
        self,
        requirment=None,
        type=None
    ):
        self.req = requirment
        self.folders = []
        self.ResultNo = 0
        self.type = type
        self.filename = []
        self.allowed = {
            "movie": [".mkv", ".mp4"]
        }

    def FileSearch(self, search):
        with open('json/FileList.json') as FolderJson:
            Folder = json.load(FolderJson)
            for x in Folder:
                if search.lower() in x['EXECUTABLE'].lower():
                    if self.type.lower() == 'movie':
                        if os.path.splitext(x['EXECUTABLE'])[1] in self.allowed["movie"]:
                            self.filename.append(
                                os.path.splitext(x['FILENAME'])[0])
                            self.folders.append(x['EXECUTABLE'])

            return [self.folders, self.filename]
# Future Expectation
# Being able to search an program more accuratly and no precise information given on it
#import subprocess
#subprocess.run('start microsoft.windows.camera:', shell=True)
#camera = subprocess.Popen('start microsoft.windows.camera:', shell=True)
# camera.terminate()  # don't work, access denied :(
