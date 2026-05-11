# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import ctypes
import json
import os
import shutil
import string
from pathlib import Path

from Security import Decryptor as De
from Security import Encryptor as En


#functions
def create_learning_code(code):  # function to create learning code
    code = code.upper()

    try:

        # connection to understand.json
        with open(
                os.path.join('Brain/FrontalLobe/understand/' +
                             'understand.json'), 'r') as all_code_collec:

            codes_in = json.load(all_code_collec)
            new_code = {code: []}
            code_index = ''
            for mon in range(len(codes_in)):
                if code in codes_in[mon]:
                    code_index = mon
            if (isinstance(code_index, int)):
                print('CODE_EXSIST')
            elif code_index == '':
                codes_in.append(new_code)
                with open(
                        os.path.join('Brain/FrontalLobe/understand/' +
                                     'understand.json'),
                        'w+') as code_collec_all:
                    frons = json.dumps(codes_in)
                    code_collec_all.write(frons)

        with open(
                os.path.join('Brain/FrontalLobe/understand/' +
                             'learning_code.json'), 'r') as sec_com:

            reptor = json.load(sec_com)
            access_code = 1
            for clumx in range(len(reptor)):
                if code == reptor[clumx]:
                    access_code = ''

            if access_code == 1:
                with open(
                        os.path.join('Brain/FrontalLobe/understand/' +
                                     'learning_code.json'), 'ab+') as main_com:
                    main_num = main_com.seek(0, 2)
                    if main_com.tell() == 2:
                        main_com.seek(-1, 2)
                        main_com.truncate()
                        main_com.write(json.dumps(str(code)).encode())
                        main_com.write(']'.encode())
                    else:
                        main_com.seek(-1, 2)
                        main_com.truncate()
                        main_com.write(' , '.encode())
                        main_com.write(json.dumps(str(code)).encode())
                        main_com.write(']'.encode())
            else:
                print('present')

        with open(os.path.join('Brain/Response/' + 'response.json'),
                  'r') as sec_collec:
            cre_op = json.load(sec_collec)
            new_resp_code = {code: [{"high": []}, {"medium": []}, {"low": []}]}
            code_count = ''
            for xes in range(len(cre_op)):
                if code in cre_op[xes]:
                    code_count = xes
            if isinstance(code_count, int):
                print("present")
            else:
                cre_op.append(new_resp_code)
                with open(os.path.join('Brain/Response/' + 'response.json'),
                          'w+') as sec_writer:
                    fro = json.dumps(cre_op)
                    sec_writer.write(fro)
        return "CODE_CREATED"
    except Exception as e:
        return e


def sen_comp(string, t_mode, code):
    with open(
            os.path.join('Brain/FrontalLobe/understand/' + 'understand.json'),
            'r') as sentences_collec:
        sentences = json.load(sentences_collec)
        index_val = 'null'
        for zxa in range(len(sentences)):
            if (code in sentences[zxa]):
                index_val = zxa
        if isinstance(index_val, int):
            ful_str = sentences[index_val]
            gs = ful_str[code]
            sen_index = 'null'

            for dun in range(len(gs)):
                jui = gs[dun]
                if jui['sentence'] == string.lower():
                    sen_index = dun
            string_res = ''
            if isinstance(sen_index, int):
                grt = gs[sen_index]
                if string.lower() == grt['sentence']:
                    string_res = 'SEN_PRESENT'
                else:
                    string_res = 'SEN_NOT_MATCHED'
            else:
                string_res = 'SEN_NOT_PRESENT'

            level_index = 'null'
            level_res = ''
            for dsa in range(len(gs)):
                jus = gs[dsa]
                if jus['level'] == t_mode.lower():
                    level_index = dsa

            if isinstance(level_index, int):
                gst = gs[level_index]
                if t_mode.lower() == gst['level']:
                    level_res = 'LEV_PRESENT'
                else:
                    level_res = 'LEV_NOT_MATCHED'
            else:
                level_res = 'LEV_NOT_PRESENT'
            fo = [string_res, level_res]
            return fo
        else:
            return 'CODE_NOT_FOUND'


def get_sen_list_f_code(code):
    with open(
            os.path.join('Brain/FrontalLobe/understand/' + 'understand.json'),
            'r') as sentences_collec:
        sentences = json.load(sentences_collec)
        index_code = ''

        for tully in range(len(sentences)):
            if code in sentences[tully]:
                index_code = tully
        sen_arr = ''
        sen_list = ''
        if isinstance(index_code, int):
            sen_arr = sentences[index_code]
            sen_list = sen_arr[code]

        else:
            sen_list = 'CODE_NOT_FOUND'

        return sen_list


def add_conv(string, t_mode, code):

    code = code.upper()

    with open(
            os.path.join('Brain/FrontalLobe/understand/' + 'understand.json'),
            'r') as new_sen:
        sen_compat = sen_comp(string, t_mode, code)

        new_sentence = {"sentence": string.lower(), "level": t_mode.lower()}

        if sen_compat == 'CODE_NOT_FOUND':
            return "CODE_NOT_FOUND"

        else:
            sen_compat = sen_comp(string, t_mode, code)

            if sen_compat[0] == 'SEN_PRESENT' and sen_compat[
                    1] == 'LEV_PRESENT':
                print('already exsists')

            if sen_compat[
                    0] == 'SEN_PRESENT' and sen_compat[1] != 'LEV_PRESENT':

                print("level not matched")

            if sen_compat[0] != 'SEN_PRESENT':

                sentences = json.load(new_sen)
                index_code = ''

                for tully in range(len(sentences)):
                    if code in sentences[tully]:
                        index_code = tully
                sen_arr = ''
                sen_list = ''
                if isinstance(index_code, int):
                    sen_arr = sentences[index_code]
                    sen_list = sen_arr[code]

                else:
                    sen_list = 'CODE_NOT_FOUND'

                if sen_list != 'CODE_NOT_FOUND':
                    sen_list.append(new_sentence)

                with open(
                        os.path.join('Brain/FrontalLobe/understand/' +
                                     'understand.json'), 'w+') as new_collec:
                    new_sen_json = json.dumps(sentences)
                    new_collec.write(new_sen_json)
                    return "SEN_CREATED"


def meaning(word):
    try:
        with open(
                os.path.join('Brain/FrontalLobe/meaning/' + 'meaning_o.json'),
                'r') as words_init:
            words = json.load(words_init)

            if word in words:
                print(f'Meaning of {word} is {words[word]}')
            else:
                print('Meaning not found!')
    except Exception as e:
        print(e)
        with open(os.path.join('Brain/FrontalLobe/words/' + 'words.txt'),
                  'r+') as word_init:
            words = set(word_init.read().split())
            if word in words:
                print('word used is present')
            else:
                print('not present')


def word_understand(word):
    try:
        with open(os.path.join('Brain/FrontalLobe/words/' + 'words.json'),
                  'r') as words_init:
            words = json.load(words_init)

            if word in words:
                print('word used is present')
            else:
                print('not present')
    except Exception as e:
        print(e)
        with open(os.path.join('Brain/FrontalLobe/words/' + 'words.txt'),
                  'r+') as word_init:
            words = set(word_init.read().split())
            if word in words:
                print('word used is present')
            else:
                print('not present')


def sen_t_code(sentence):
    with open(
            os.path.join('Brain/FrontalLobe/understand/' + 'understand.json'),
            'r') as sen_collec:
        with open(
                os.path.join('Brain/FrontalLobe/understand/' +
                             'learning_code.json'), 'r') as code_collec:
            fron_sen = json.load(sen_collec)
            fron_code = json.load(code_collec)
            code_sen = ''
            sen_count = ''
            sen_level = ''
            for pros in range(len(fron_sen)):
                code_sen = fron_sen[pros]
                code_col_m = fron_code[pros]
                jer = code_sen[code_col_m]
                for glim in range(len(jer)):
                    cream = jer[glim]
                    if cream['sentence'] in sentence.lower():
                        sen_count = pros
                        sen_level = cream['level']
            if sen_count != '':
                return [fron_code[sen_count], sen_level]
            else:
                return 'X'


def sen_avail(sentence):
    sentence = sentence.lower()
    with open(
            os.path.join('Brain/FrontalLobe/understand/' + 'understand.json'),
            'r') as senr:
        with open(
                os.path.join('Brain/FrontalLobe/understand/' +
                             'learning_code.json'), 'r') as secr:
            crip = json.load(senr)
            vro = json.load(secr)
            sen_count = ''
            for vec in range(len(crip)):
                brp = crip[vec]

                vrs = brp[vro[vec]]

                for cles in range(len(vrs)):
                    vopr = vrs[cles]
                    if vopr['sentence'] in sentence:
                        sen_count = vec

        if isinstance(sen_count, int):
            return "SEN_EXSISTS"
        else:
            return "SEN_NOT_EXSISTS"


def sen_def(sen):
    sen = sen.lower()
    rtp = sen_avail(sen)
    sen_pr = ''
    if rtp == "SEN_NOT_EXSISTS":
        with open(
                os.path.join('Brain/FrontalLobe/understand/' +
                             'unexplained.json'), 'r') as jrop:
            crm = json.load(jrop)
            for vtp in crm:
                if sen == vtp['Q']:
                    sen_pr = vtp
            if (isinstance(sen_pr, int)):
                return "SEN_PRESENT"
            else:
                crm.append({"Q": sen})
                with open(
                        os.path.join('Brain/FrontalLobe/understand/' +
                                     'unexplained.json'), 'w+') as furge:
                    brp = json.dumps(crm)
                    furge.write(brp)
    else:
        return "SEN_IN_LIST"


def code_com(e):
    with open(
            os.path.join('Brain/FrontalLobe/understand/' +
                         'learning_code.json'), 'r') as frio:
        sve = json.load(frio)
        frp = ''
        for uis in range(len(sve)):
            if e == sve[uis]:
                frp = uis
        if frp == '':
            return 'CODE_NOT_PRESENT'
        else:
            return 'CODE_PRESENT'


def sen_comp(string, t_mode, code):
    with open(
            os.path.join('Brain/FrontalLobe/understand/' + 'understand.json'),
            'r') as sentences_collec:
        sentences = json.load(sentences_collec)
        index_val = 'null'
        for zxa in range(len(sentences)):
            if (code in sentences[zxa]):
                index_val = zxa
        if isinstance(index_val, int):
            ful_str = sentences[index_val]
            gs = ful_str[code]
            sen_index = 'null'

            for dun in range(len(gs)):
                jui = gs[dun]
                if jui['sentence'] == string.lower():
                    sen_index = dun
            string_res = ''
            if isinstance(sen_index, int):
                grt = gs[sen_index]
                if string.lower() == grt['sentence']:
                    string_res = 'SEN_PRESENT'
                else:
                    string_res = 'SEN_NOT_MATCHED'
            else:
                string_res = 'SEN_NOT_PRESENT'


#classes
class FileHandler:
    def FileJsonResp(file):  # return json structure from filename type
        file = file.upper()
        if file == 'FILE_UNDERSTAND':  # understand json file
            with open(
                    os.path.join('Brain/FrontalLobe/understand/' +
                                 'understand.json'),
                    'r') as UnderstandActuator:
                UnderstandJson = json.load(UnderstandActuator)
                return UnderstandJson
        if file == 'FILE_UNEXPLAINED':  # understand json file
            with open(
                    os.path.join('Brain/FrontalLobe/understand/' +
                                 'unexplained.json'), 'r') as UnSenActuator:
                UnexplainedJson = json.load(UnSenActuator)
                return UnexplainedJson
        if file == 'FILE_CODE':  # learning code json file
            with open(
                    os.path.join('Brain/FrontalLobe/understand/' +
                                 'learning_code.json'),
                    'r') as LearningCodeActuator:
                LearningCodeJson = json.load(LearningCodeActuator)
                return LearningCodeJson
        if file == 'FILE_RESPONSE':  # Response json file
            with open(os.path.join('Brain/Response/' + 'response.json'),
                      'r') as ResponseActuator:
                ResponseJson = json.load(ResponseActuator)
                return ResponseJson
        if file == 'FILE_JRESPONSE':  # jresponse json file
            with open(
                    os.path.join('Brain/Limbic/JResponse/' + 'jresponse.json'),
                    'r') as JResponseActuator:
                JResponseJson = json.load(JResponseActuator)
                return JResponseJson
        if file == 'FILE_AUTH':  # Auth json file
            with open(os.path.join('Brain/Limbic/sn/auth/' + 'u.json'),
                      'r') as AuthActuator:
                AuthJson = json.load(AuthActuator)
                return AuthJson

    def FileJsonWri(file, content):  # return json write
        file = file.upper()
        if file == 'FILE_UNDERSTAND':  # understand json file
            with open(
                    os.path.join('Brain/FrontalLobe/understand/' +
                                 'understand.json'), 'w+') as UnSenActuator:
                UnexplianedJsonMain = json.dumps(content)
                UnSenActuator.write(UnexplianedJsonMain)
        if file == 'FILE_UNEXPLAINED':  # understand json file
            with open(
                    os.path.join('Brain/FrontalLobe/understand/' +
                                 'unexplained.json'),
                    'w+') as UnderstandActuator:
                UnderstandJsonMain = json.dumps(content)
                UnderstandActuator.write(UnderstandJsonMain)
        if file == 'FILE_CODE':  # learning code json file
            with open(
                    os.path.join('Brain/FrontalLobe/understand/' +
                                 'learning_code.json'),
                    'ab+') as LearningCodeActuator:
                if LearningCodeActuator.tell(
                ) == 2:  # check if the size of the file is 2
                    # deleting the last bracket
                    LearningCodeActuator.seek(-1, 2)
                    LearningCodeActuator.truncate(
                    )  # setting the size of the file
                    LearningCodeActuator.write(
                        json.dumps(
                            str(content)).encode())  # appending the content
                    LearningCodeActuator.write(
                        ']'.encode())  # adding last bracket
                else:  # if the json is not empty
                    LearningCodeActuator.seek(-1, 2)  # deleting last bracket
                    LearningCodeActuator.truncate(
                    )  # setting the size to the by removing 1 bytes
                    LearningCodeActuator.write(
                        ' , '.encode())  # appending the ,
                    LearningCodeActuator.write(
                        json.dumps(
                            str(content)).encode())  # adding the content
                    # closing the file by bracket
                    LearningCodeActuator.write(']'.encode())
        if file == 'FILE_RESPONSE':  # Response json file
            with open(os.path.join('Brain/Response/' + 'response.json'),
                      'w+') as ResponseActuator:
                ResponseJsonMain = json.dumps(content)
                ResponseActuator.write(ResponseJsonMain)
        if file == 'FILE_JRESPONSE':  # jresponse json file
            with open(
                    os.path.join('Brain/Limbic/JResponse/' + 'jresponse.json'),
                    'w+') as JResponseActuator:
                JResponseJsonMain = json.dumps(content)
                JResponseActuator.write(JResponseJsonMain)

    def FileCodeCheck():

        LearningCodeJson = FileHandler.FileJsonResp('FILE_CODE')
        UnderstandJson = FileHandler.FileJsonResp('FILE_UNDERSTAND')
        ResponseJson = FileHandler.FileJsonResp('FILE_RESPONSE')

        if len(LearningCodeJson) == len(UnderstandJson):
            if len(LearningCodeJson) == len(ResponseJson):
                return 1
            else:
                return 0
        else:
            return 2

    def FileJsonChecker():

        LearningCodeJson = FileHandler.FileJsonResp('FILE_CODE')
        UnderstandJson = FileHandler.FileJsonResp('FILE_UNDERSTAND')
        ResponseJson = FileHandler.FileJsonResp('FILE_RESPONSE')
        CodeArr = []
        ResArr = []
        MainArr = []
        FileCheck = FileHandler.FileCodeCheck()
        if FileCheck == 1:
            for x in LearningCodeJson:
                CodeStat = False
                CodeArr.append(x in UnderstandJson[LearningCodeJson.index(x)])
                ResArr.append(x in ResponseJson[LearningCodeJson.index(x)])
                if x in UnderstandJson[LearningCodeJson.index(x)]:
                    if x in ResponseJson[LearningCodeJson.index(x)]:
                        CodeStat = True
                MainArr.append(CodeStat)

            if CodeArr == ResArr:
                if len(set(MainArr)) == 1:
                    return 1
            else:
                return 0

    def __FileLogger__(name):  # it is an array
        dirs = []
        tempPath = []
        tempSan = []
        continuing = False
        paths = []
        with os.scandir(name) as sandir:
            while True:
                try:
                    entry = next(sandir)
                except StopIteration:
                    break
                try:
                    sid = Path(entry).is_dir()
                except:
                    sid = False
                if sid:
                    dirs.append(entry.name)
                    tempPath.append(entry.path)
                    tempSan.append(entry)
                    continuing = True
            if continuing:
                for x in tempPath:
                    with os.scandir(x) as NewSan:
                        while True:
                            try:
                                Dentry = next(NewSan)
                            except StopIteration:
                                break
                            try:
                                ssid = Path(Dentry).is_dir()
                            except:
                                ssid = False
                            if ssid:
                                dirs.append(Dentry.name)
                                tempPath.append(Dentry.path)
                                paths.append(Dentry.path)
                                continuing = True
            return [paths, dirs]

    def AllFiles(name):
        AllFiles = []
        name = FileHandler.__FileLogger__(name + '/')
        for path in name[0]:
            AllFiles.append(path)
        return AllFiles

    def FileBackup():
        FileTest = FileHandler.AllFiles('.')
        FileJarvis = FileHandler.AllFiles('Jarvis')
        FileTestHome = os.listdir('.')
        FileJarvisHome = os.listdir('Jarvis')
        FileNewDirectory = []
        AllFiles = []
        Alldirs = []
        for x in FileTestHome:
            FileName = './' + x
            SplitFiles = os.path.splitext(x)
            if Path(FileName).is_dir():
                Alldirs.append(x)
                if not Path('Jarvis/' + x).is_dir():
                    if x != '.pytest_cache' or x != '.vscode' or x != '__pycache__':
                        os.mkdir('Jarvis/' + x)
                AllInitFile = os.listdir(FileName)
                for k in AllInitFile:
                    SplitExtention = os.path.splitext(k)
                    if SplitExtention[1] != '':
                        NewFileChanger = FileName.split('/')
                        NewFileChanger[1] = 'Jarvis'
                        NewFileName = '/'.join(NewFileChanger)
                        shutil.copy(FileName + '/' + k, NewFileName + '/')
            if SplitFiles[1] == '.py' or SplitFiles[
                    1] == '.json' or SplitFiles[1] == '.txt':
                shutil.copy(FileName, 'Jarvis')
                AllFiles.append(x)
        for z in FileTest:
            SplitDirectory = z.split('/')
            MSplitDirectory = z.split('/')
            MSplitDirectory[0] = ''
            MSplitDirectory[1] = ''
            SplitDirectory[1] = 'Jarvis'
            FullDirectory = '/'.join(SplitDirectory)
            DirectroyList = os.listdir(z)
            Alldirs.append(FullDirectory)
            if not Path(FullDirectory).is_dir():
                os.mkdir(FullDirectory)
            FDirectory = FullDirectory.replace('\ '[:-1], '/') + '/'
            DDirectory = z.replace('\ '[:-1], '/') + '/'
            for y in DirectroyList:
                SplitExten = os.path.splitext(y)
                if SplitExten[1] == '.py' or SplitExten[
                        1] == '.json' or SplitExten[1] == '.txt':
                    shutil.copy(DDirectory + y, FDirectory + '/')
                    AllFiles.append(y)
        print('Pannel Backuped')

    def PenChecker():
        Drives = ['H', 'I', 'J']
        ActiveDrive = []
        AllDrvieMain = []
        for x in Drives:
            if os.path.exists(x + ':/'):
                ActiveDrive.append(x + ':/')
                AllDrvieMain.append(x)
        # Access check
        for y in ActiveDrive:
            DriveLIST = os.listdir(y)
            for z in DriveLIST:
                if z == 'Jarvis':
                    NewList = os.listdir(y + 'Jarvis/')
                    if 'a.json' in NewList:
                        return True
                if z != 'Jarvis':
                    return False

    def PenDriveBackup():
        Drives = ['H', 'I', 'J']
        ActiveDrive = []
        AllDrvieMain = []
        AccessType = False
        for x in Drives:
            if os.path.exists(x + ':/'):
                ActiveDrive.append(x + ':/')
                AllDrvieMain.append(x)
        # Access check
        for y in ActiveDrive:
            DriveLIST = os.listdir(y)
            for z in DriveLIST:
                if z == 'Jarvis':
                    NewList = os.listdir(y + 'Jarvis/')
                    if 'a.json' in NewList:
                        OwnJson = json.load(
                            open('Brain/Limbic/sn/auth/u.json'))
                        Json = open(y + 'Jarvis/' + 'a.json')
                        JsonRead = json.load(Json)
                        AccessCode = JsonRead['USER_ACCESS_CODE']
                        OwnAccess = OwnJson['USER_ACCESS_CODE']

                        if De.DoDecrypt(AccessCode) == OwnAccess:
                            NewFiler = y[:-2]
                            AccessType = True
                            FileTest = FileHandler.AllFiles('.')
                            FileJarvis = FileHandler.AllFiles(y + 'Jarvis')
                            FileTestHome = os.listdir('.')
                            FileJarvisHome = os.listdir(y + 'Jarvis')
                            FileNewDirectory = []
                            AllFiles = []
                            Alldirs = []
                            for x in FileTestHome:
                                FileName = './' + x
                                SplitFiles = os.path.splitext(x)
                                if Path(FileName).is_dir():
                                    Alldirs.append(x)
                                    if not Path(y + '/Jarvis/' + x).is_dir():
                                        if x != '.pytest_cache' or x != '.vscode' or x != '__pycache__':
                                            os.mkdir(y + 'Jarvis/' + x)
                                    AllInitFile = os.listdir(FileName)
                                    for k in AllInitFile:
                                        SplitExtention = os.path.splitext(k)
                                        if SplitExtention[1] != '':
                                            NewFileChanger = FileName.split(
                                                '/')
                                            NewFileChanger[0] = NewFiler + ':'
                                            NewFileChanger[1] = 'Jarvis'
                                            NewFileName = '/'.join(
                                                NewFileChanger)
                                            shutil.copy(
                                                FileName + '/' + k,
                                                NewFileName + '/')
                                if SplitFiles[1] == '.py' or SplitFiles[
                                        1] == '.json' or SplitFiles[
                                            1] == '.txt':
                                    shutil.copy(FileName, y + 'Jarvis')
                                    AllFiles.append(x)
                            for z in FileTest:
                                SplitDirectory = z.split('/')
                                MSplitDirectory = z.split('/')
                                MSplitDirectory[0] = ''
                                MSplitDirectory[1] = ''
                                SplitDirectory[0] = NewFiler + ':'
                                SplitDirectory[1] = 'Jarvis'
                                FullDirectory = '/'.join(SplitDirectory)
                                DirectroyList = os.listdir(z)
                                Alldirs.append(FullDirectory)
                                if not Path(FullDirectory).is_dir():
                                    os.mkdir(FullDirectory)
                                FDirectory = FullDirectory.replace(
                                    '\ '[:-1], '/') + '/'
                                DDirectory = z.replace('\ '[:-1], '/') + '/'
                                for y in DirectroyList:
                                    SplitExten = os.path.splitext(y)
                                    if SplitExten[1] == '.py' or SplitExten[
                                            1] == '.json' or SplitExten[
                                                1] == '.txt':
                                        shutil.copy(DDirectory + y,
                                                    FDirectory + '/')
                                        AllFiles.append(y)
                            print('File backup uploaded')
                            return AccessType


class CSentence:
    def codeCheck(code):  # checks codes availibility in the learning code
        code = code.upper()  # assigning code upper case
        CodePresence = False  # variable for code avalibility False by Default
        LearningCodeJson = FileHandler.FileJsonResp(
            'FILE_CODE')  # learning code json file
        IndexNumber = ''  # index for code in the learning code
        for x in LearningCodeJson:
            if x == code:
                CodePresence = True  # assigning true if the code is present in learning code
                IndexNumber = LearningCodeJson.index(code)
        if CodePresence:
            # return present if code is present
            return ['CODE_PRESENT', IndexNumber]
        else:
            return ['CODE_N_PRESENT']  # return not present

    def senCheck(sentence):  # check for sentence in understand json
        LearningCodeJson = FileHandler.FileJsonResp(
            'FILE_CODE')  # learning code json file
        UnderstandJson = FileHandler.FileJsonResp(
            'FILE_UNDERSTAND')  # understand json
        sentence = sentence.lower()
        SenAva = False  # setting sentence ava to false by default
        CodeIndex = ''  # Index of the code in understand json
        SentenceIndex = ''  # Index of the sentence in understand json
        for x in range(len(UnderstandJson)):
            LearningCode = LearningCodeJson[x]  # learning code from index
            # setting sentence list from code
            UnderstandSen = UnderstandJson[x][LearningCode]

            for y in UnderstandSen:  # understand code sentence list`
                if y['sentence'] in sentence:  # presence of written sentence in the assigned variable
                    SenAva = True
                    CodeIndex = x
                    SentenceIndex = y

        if SenAva:
            return ['SEN_PRESENT', CodeIndex, SentenceIndex]
        else:
            return ['SEN_N_PRESENT']

    def UnderstandJsonCheck(code, sentence, level):

        UnderstandJson = FileHandler.FileJsonResp(
            'FILE_UNDERSTAND')  # understand json
        code = code.upper()  # setting code to upper case
        sentence = sentence.lower()  # setting sentence to lower
        level = level.lower()  # setting level to lower
        SenAva = False  # availibility of the code and sentence
        FinalAva = False  # Final availibility default false
        ListNumber = ''  # by default the vale of list none
        FeedBack = ''  # collect feedback incase of problem by default none
        CodeCheck = CSentence.codeCheck(code)  # return array
        SenCheck = CSentence.senCheck(sentence)  # return array

        if CodeCheck[0] == 'CODE_PRESENT':
            if SenCheck[0] == 'SEN_PRESENT':
                # codecheck with index 1 return the index of code in the list of understandjson
                CodeIndex = CodeCheck[1]
                CodeList = UnderstandJson[CodeIndex][code]  # return code list

                for x in CodeList:
                    if x['sentence'] in sentence:  # from code list matching for sentence presence
                        SenAva = True  # true if matched
                        ListNumber = CodeList.index(x)  # setting index number
                if SenAva:
                    SenLevel = CodeList[ListNumber]['level']
                    if SenLevel == level:
                        FinalAva = True
                    else:
                        FeedBack = 'LEVEL_NOT_MATCHED'
            else:
                FeedBack = 'SEN_NOT_PRESENT'
        else:
            FeedBack = 'CODE_NOT_PRESENT'
        if FinalAva:
            return 'FINAL_MATCHED'
        else:
            return FeedBack

    def Jauth():
        AuthJsonActuator = open(
            os.path.join('Brain/Limbic/sn/auth/' + 'auth_action.json'), 'r')
        JsonLoadAuth = json.load(AuthJsonActuator)
        AuthStat = JsonLoadAuth['AuthAction']
        return De.DoDecrypt(AuthStat)


class ESentence:
    def SentenceTC(sentence):
        sentence = sentence.lower()  # converting sentence to lower
        LearningCodeJson = FileHandler.FileJsonResp(
            'FILE_CODE')  # learning code json
        UnderstandJson = FileHandler.FileJsonResp(
            'FILE_UNDERSTAND')  # understand json
        SentenceCheck = CSentence.senCheck(sentence)  # return array
        UnIndex = ''
        SenIndex = ''
        if SentenceCheck[0] == 'SEN_PRESENT':
            UnIndex = SentenceCheck[1]  # index of code in understand json
            SenIndex = SentenceCheck[2]  # sentence element in the list
            LearningCode = LearningCodeJson[UnIndex]
            return [LearningCode, SenIndex['level']]
        else:
            return 'X'


class WSentence:
    def CreateLC(code):  # create leraning code
        code = code.upper()
        UnderstandJson = FileHandler.FileJsonResp('FILE_UNDERSTAND')
        ResponseJson = FileHandler.FileJsonResp('FILE_RESPONSE')
        CodeCheck = CSentence.codeCheck(code)
        UnderstanNewShell = {code: []}  # understand json shell code creation
        # response json shell code creation
        ResponseNewShell = {code: [{"high": []}, {"medium": []}, {"low": []}]}

        if CodeCheck[0] == 'CODE_N_PRESENT':
            UnderstandJson.append(UnderstanNewShell)
            ResponseJson.append(ResponseNewShell)
            FileHandler.FileJsonWri('FILE_CODE', code)
            FileHandler.FileJsonWri('FILE_RESPONSE', ResponseJson)
            FileHandler.FileJsonWri('FILE_UNDERSTAND', UnderstandJson)
            return 'CODE_CREATED'

    def CreateSen(code, sentence, level):  # add sentence to understand json
        code = code.upper()
        level = level.lower()
        sentence = sentence.lower()
        UnderstandJson = FileHandler.FileJsonResp('FILE_UNDERSTAND')
        LearningCodeJson = FileHandler.FileJsonResp('FILE_CODE')
        UnderstandCheck = CSentence.UnderstandJsonCheck(
            code, sentence, level)  # check for all sentence presence
        CodeCheck = CSentence.codeCheck(code)
        SentenceShell = {
            'sentence': sentence,
            'level': level
        }  # new sentence shell

        if UnderstandCheck == 'SEN_NOT_PRESENT':
            if CodeCheck[0] == 'CODE_PRESENT':
                LearningCode = LearningCodeJson[CodeCheck[1]]
                SenList = UnderstandJson[CodeCheck[1]][LearningCode]
                SenList.append(SentenceShell)
                FileHandler.FileJsonWri('FILE_UNDERSTAND', UnderstandJson)
                return 'SEN_CREATED'

    def UndefinedSen(sentence):
        sentence = sentence.lower()
        SenCheck = CSentence.senCheck(sentence)
        UnexplainedJson = FileHandler.FileJsonResp('FILE_UNEXPLAINED')
        UnSenShell = {'Q': sentence}
        if SenCheck[0] == 'SEN_N_PRESENT':
            if UnSenShell not in UnexplainedJson:
                if sentence != '' or sentence != ' ':
                    UnexplainedJson.append(UnSenShell)
                    FileHandler.FileJsonWri('FILE_UNEXPLAINED',
                                            UnexplainedJson)

    def Jauth(text):
        text = text.lower()
        AuthJsonActuator = open(
            os.path.join('Brain/Limbic/sn/auth/' + 'auth_action.json'), 'w+')
        NewAuth = {"AuthAction": En.DoEncryptor(text)}
        JsonDump = json.dumps(NewAuth)
        AuthJsonActuator.write(JsonDump)
        return True


#new end to the addition of broca_area
