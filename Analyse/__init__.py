# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import ast
import json
import os
import pprint as ps
import shutil
import sqlite3
import time
import webbrowser
import request
import selenium
from requests_html import HTMLSession

import urllib

'''
In this script i will most probably create a web page analyser and made the script readable and apply Cortex realtime data

'''

class Webaction():
    def __init__(self,url):
        self.url = url
        self.content = ""
        self.ClassArray = []
        self.idArray = []
        self.subordinates = []
        self.childrens = []
        self.isload = False
        self.ScriptCount = 0
        self.isjs = False
        self.jsArray = []
        self.language = "HTML"
        self.extensionType = ".html"
        self.name = (str(time.gmtime().tm_wday)+'-'+str(time.gmtime().tm_hour)+'-'+str(time.gmtime().tm_min)+'-'+str(time.gmtime().tm_sec))
    def loadPage(self):
        m = urllib.request.urlopen(self.url)
        self.content = str(m.read())
        self.isload = True
        return self.isload
    def CopySection(self):
        self.loadPage()
        if self.isload == True:
            with open(os.path.join("analyse/"+self.name+".txt"),"w+") as Copyer:
                Copyer.write(self.content)
                print("copy success")
m = Webaction("https://google.com/search?q=hello")
m.CopySection()