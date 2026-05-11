# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

#!usr/bin/env python3
import ast
import json
import os
import pprint as ps
import shutil
import sqlite3
import time
import webbrowser
import sys
import subprocess
import platform

import selenium
from requests_html import HTMLSession

session = HTMLSession()
suf = ['ON', 'BY', 'IN', 'OF', 'FOR']


def searchWebsite(WebsiteName, SearchText):
    #from google + ,facebook search/top/?q= %20 twitter search?q= %20, youtube = results?search_query = + ,wikipedia.org = /w/index.php?search=, amazon = /s?k=i+m
    with open(
            os.path.join(
                'Brain/FrontalLobe/response/application/application.json')
    ) as WebAppColl:
        webCollec = json.load(WebAppColl)
        website = ''
        for x in webCollec:
            if x['TYPE'] == 'WEBSITE':
                if WebsiteName.upper() == x['NAME']:
                    if 'SPATH' in x:
                        webSearchFinal = SearchText.replace(' ', x['STYPE'])
                        website = x['PATH'] + x['SPATH'] + webSearchFinal
                        webbrowser.open_new(website)
def searchAppSpec(sentence):
    sentence = sentence.upper()
    try:
        with open(
                os.path.join('Brain/FrontalLobe/understand/' +
                             'understand.json')) as ASearch:
            SearchIn = json.load(ASearch)
            SearchCro = SearchIn[7]['SEARCH_PRI_ACTION']
            for x in SearchCro:
                if x['sentence'] in sentence.lower():
                    SearchSplit = sentence.upper().split(
                        x['sentence'].upper() + ' ')
                    with open(
                            os.path.join(
                                'Brain/FrontalLobe/response/application/application.json'
                            )) as SearchApplo:
                        SearchRes = json.load(SearchApplo)
                        Ss = ''
                        SType = 'WEBSITE'
                        SSearchName = 'GOOGLE'
                        SearchFinal = ''
                        webSplit = SearchSplit[1]
                        for y in SearchRes:
                            if y['NAME'] in sentence.upper():
                                if y['NAME'] in SearchSplit[1]:
                                    senIn = SearchSplit[1].split(' ')
                                    for z in suf:
                                        if z in senIn[-2]:
                                            SearchFinal = SearchSplit[1].split(
                                                ' ' + z + ' ')
                                            webSplit = SearchFinal[0]
                                        if z in senIn[-3]:
                                            SearchFinal = SearchSplit[1].split(
                                                ' ' + z + ' ')
                                            webSplit = SearchFinal[0]
                                SSearchName = y['NAME']
                                Ss = y['PATH']
                                SType = y['TYPE']
                        if SType == 'WEBSITE':
                            searchWebsite(SSearchName, webSplit.lower())
                    return 1
    except:
        return 0
def acOpner(sen):
    try:
        sentence = sen.upper()
        with open(
                os.path.join(
                    'Brain/FrontalLobe/response/application/application.json')
        ) as acResponse:
            appRes = json.load(acResponse)
            xs = ''
            xType = ''
            xSearchName = ''
            for x in appRes:
                try:
                    if x['NAME'] in sentence:
                        xSearchName = x['NAME']
                        xs = x['PATH']
                        xType = x['TYPE']
                except:
                    return 0
            if xType == 'WEBSITE':
                webbrowser.open_new(xs)
                print('opening sir...')
            if xType == 'PYTHON':
                # Cross-platform application launcher
                if platform.system() == 'Windows':
                    os.system(f'start {xs}')
                elif platform.system() == 'Darwin':  # macOS
                    subprocess.Popen(['open', xs])
                else:  # Linux and others
                    subprocess.Popen([xs])
                print('opening sir...')
            if xType == 'APPLICATION':
                # Cross-platform application launcher
                if platform.system() == 'Windows':
                    os.system(f'start {xs}')
                elif platform.system() == 'Darwin':  # macOS
                    subprocess.Popen(['open', xs])
                else:  # Linux and others
                    subprocess.Popen([xs])
                print('opening sir...')
        return 1
    except:
        return 0
def SearchAbout(text):
    takin = ''
    indexval = 0
    if "about" in text:
        if "Cortex" not in text or "yourself" not in text:
            text = text.split("about ")[1]
            if " " in text:
                text = text.replace(" ", "_")
            if not " " in text:
                text = text
            wiki = session.get('https://en.wikipedia.org/wiki/' + text)
            init = wiki.html.find('p')
            if len(init) > 5:
                for x in range(0, 2):
                    if init[x].text == "" or init[x].text == " ":
                        print(init[x + 1])
                        indexval = indexval + 1
                    if init[x].text != "" or init[x].text != " ":
                        print(init[x].text)
                        indexval += 1
                takin = input('Y/y>')
                if takin.lower() == 'y':
                    for y in range(indexval, len(init) - 1):
                        print(init[y].text)
def GetHistoryToLocalStorage():
    try:
        data_path = os.path.expanduser(
            '~') + "/AppData/Local/Google/Chrome/User Data/Default"
        files = os.listdir(data_path)

        history_db = os.path.join(data_path, 'history')
        shutil.copy(history_db, "Database/")
        return "COPY_SUCCESS"
    except:
        return "COPY_FAIL"
#recreational swift to the identical node of data creation
def ReadHistoryOfLocalStorage():
    ReturnGet = GetHistoryToLocalStorage()
    AllReturnArray = []
    if ReturnGet == "COPY_SUCCESS":
        db = os.path.join("Database/", "history")

        DBConnection = sqlite3.connect(db)
        CourS = DBConnection.cursor()

        ConnectionExec = CourS.execute(
            "SELECT * FROM urls, visits WHERE urls.id = visits.url;")
        ExecResult = CourS.fetchall()
        #AllReturnArray.append(ps.pformat(ExecResult))
        ExCop = ps.pformat(ExecResult, 0)
        return ExCop
def PrepHistoryRead(inp):
    newArr = ast.literal_eval(inp)
    return newArr
def MainReadExe():
    NamePathArr = []
    AllNameArr = []
    db = PrepHistoryRead(ReadHistoryOfLocalStorage())
    for x in db:
        AllNameArr.append(x[2])
        NamePathArr.append(x[1])
    time.sleep(5)
    NamePath = NamePathArr[::-1]
    time.sleep(10)
    AllArr = AllNameArr[::-1]
    return [AllArr, NamePath]
def ApUse():
    Reading = json.load(open("json/appUse.json"))
    m = MainReadExe()
    AllSmpLink = []
    AllSimpArray = []
    for y in m[1]:
        for x in Reading:
            if x in y:
                AllSimpArray.append(m[0][int(m[1].index(y))])
                AllSmpLink.append(m[1][int(m[1].index(y))])
    webbrowser.open_new(AllSmpLink[0])
