# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

#!/usr/bin/env python3
import os
import json
import sqlite3
import platform
import sys
import datetime
import time
import math
import getpass
import shutil
import calendar

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))

from Jdecrypt import Decryptor as _
__stage__ = 1
__version__ = '0.0.1'

__all__ = ["auth","log","exTRaction","fcheck","Reader"]

file = os.path.abspath(__file__).replace(os.path.basename(__file__),'')

def auth():
    pwd = getpass.getpass("password: ")
    opwd = json.load(open(file+'.init/action.json'))['AUTH']
    if pwd == _(opwd):
        return 1
    else:
        return 0
def log(sen):
    with open(file+'.log/package.log','a+') as log:
        log.write(sen+"\n")
def exTracion(name):
    cname = list(name)
    rextension = [] #extension in reverse form
    extensionarr = []
    extension = ''
    for x in range(0,len(cname)):
      ran = (len(cname)-1)-x
      rextension.append(cname[ran])
      if cname[ran] == '.':
         break
    
    for y in range(0,len(rextension)):
      rran = (len(rextension)-1)-y
      if rextension[rran] != '.':
        extensionarr.append(rextension[rran])
    
    extension = ''.join(extensionarr)

    return extension
def fcheck(name):
    #special checking algorithm for the files
    #here name is the directory and file name so i will neglect the last file/folder name and try to check whether it exsists or not
    file = ''
    
    arr = name.split('/') #basically
    lname = arr[-1] #file or folder name
    narr = []
    pall = [] #collection of all the posibilities
    static = 0
    nwx=''
    #the remove function was not working for me so i am using the old method
    for a in arr:
        if a != lname:
            narr.append(a)
    folder = '/'.join(x for x in narr)
    #only for linux based
    collection = os.listdir('/'+folder)
    for x in collection:
        #here x might be a file but name has no extension so
        
        if os.path.isfile(folder+'/'+x):
            ex = exTracion(x)
            nwx = x.replace('.'+ex,'')
        
        if not os.path.isfile(folder+'/'+x):
            nwx = x
        
        if lname == nwx: #checking wheather it share some resemblencse
            #now making the list of all the possiblities
            #now the equal names can be both folder or file so we need to as the user about that 
            #for only linux
            #just checking
            if os.path.isfile(folder+'/'+x):
                #the name is a file
                static+= 1
                pall.append(folder+'/'+x)
            if os.path.isdir('/'+folder+'/'+x):
                #the name is a folder
                static+= 1
                pall.append(folder+'/'+x)
            #making sure
            if static == 2:
                #both the folder and file with same name must exsists
                return [1,pall]
            if static == 1:
                if os.path.isfile('/'+folder+'/'+x):
                            #the name is a file
                            return ["file",folder+'/'+x]
                if os.path.isdir('/'+folder+'/'+x):
                    #the name is a folder
                    return ["dir",folder+'/'+x]
            else:
                #if none then
                return [0,"none"]

class Reader():
  
    def __init__(self,stage): #here stage implies the data processing stage it can be used in the jconsole later 
        
        self.name = '' #none by default
        self.state = 'N' #'U' for upload anf 'R' to remove and 'D' for download maily used for download
        self.stage = stage
    
        self.type = 'D' #Directory as default
        self.pfile = '' 
        self.stat = 0 #number of tries
        self.contents = ''
        self.dtn = '/home/stark/Test/jpm/.packages/' #destination folder 
        self.file = {
                "dependency":" ",
                "init":{
                    "name": ' ',
                    "author": ' ',
                    "version": ' ',
                    "details": {
                        "last_modified": '',
                        "os": ' ',
                        "location": ' ', 
                        "extension": ' ',
                        "privacy": 0,
                        "message": ' '
                    }
                }
        }
        
        self.auth = 0
    def preader(self):
       
        #solely dedicated to read the data of the files in a folder
        #from the init we can get the dir package name in the location of the file with the user os
        print("Starting scan...")
        if os.path.exists(self.pfile):
            #the assumption of the package name and folder name is right then procced
            #then just copy the whole folder
            self.contents = self.pfile    

        if not os.path.exists(self.pfile):
            
            #if not exsists then
            uinput = input("Trouble in finding the location of the folder is given name is a file [y/n]: ")
            if self.stat != 2: #maximum two tries
                if uinput.lower() == 'y':
                    #provided name is a file
                    #checking for the exsistence of the file
        
                    if os.path.isfile(self.pfile):
                        #ok it exsists execute the command
                        self.type = 'F' #type is file
                        self.contents = self.pfile
                    else:
                        #need the data
                        location = input("location: ")
                        folder = input("file name: ")
                        self.pfile = location+'/'+folder
                        self.stat+=1
                        self.preader()

                if uinput.lower() == 'n':
                    #provided name does not exsists in user directory
                    location = input("location: ")
                    folder = input("folder name: ")
                    self.pfile = location+'/'+folder
                    self.stat+=1
                    self.preader()
            if self.stat == 2:
                print("Sorry please try agian after sometime")
    def ftransfer(self):
      if self.state == 'U':
        types = fcheck(self.pfile)[0]
        name = fcheck(self.pfile)[1] #name
        nwx = []
        self.preader()
        if types == 'dir':
            print('uploading ...')
            shutil.copytree(name,self.dtn+self.file['init']['name'])
            print("\x1b[32m success")
        if types == 'file':
            shutil.copyfile(name,self.dtn+os.path.basename(name))
            print('uploading ...')
            print("\x1b[32m success")
        if types == 0:
            shutil.copyfile(name,self.dtn+os.path.basename(name))
            print("\x1b[31m fail")
      
      if self.state == 'R':
          #remove files from the destination folder
          flist = os.listdir(self.dtn)
          for x in flist:
                   
            if os.path.isfile(self.dtn+x):
                ex = exTracion(x)
                nwx = x.replace('.'+ex,'')
      
            if os.path.isdir(self.dtn+x):
                nwx = x
      
            if self.name == nwx: 
          
                    print('starting ...')
                    check = fcheck(self.dtn+self.name)[0]
                    oname = fcheck(self.dtn+self.name)[1]
                    if check == 'dir':
                        print('detected ...')
                        shutil.rmtree(oname)
                        print("\x1b[32msuccess")
                    if check == 'file':
                        print('detected ...')
                        os.remove(oname)
                        print("\x1b[32msuccess")
                    if check == 0:
                        print('not found ...')
                        print("\x1b[31m fail")
    def upload(self,name):

        self.name = name
        self.state = 'U'
        
        #insertion of data
        #inserted data is a folder so
        # how to process data from a folder        
        try:   
            self.file['init']['details']['os']  = platform.system()
            self.file['init']['name'] = name
            self.file['dependency'] = f'{name}@jpm'
            self.file['init']['author'] = str(input("Author: "))
            self.file['init']['version'] = str(input("Version: "))
            self.file['init']['details']['last_modified'] = str(input("Last modified: "))
            self.file['init']['details']['location'] = str(input("Location: "))
            self.file['init']['details']['extension'] = str(input("Extension: "))
            self.file['init']['details']['privacy'] = int(input("Privacy code: "))
            self.file['init']['details']['message'] = str(input("Message: "))
            
            #add data to json

            try:
                readata = json.load(open('.jpm/package.json'))

            except:
                readata = json.loads(open('.jpm/package.json'))

                readata.append(self.file)

            with open('.jpm/package.json','w+') as init:
                data = json.dumps(readata)
                init.write(data)
            
            #add data to database

            db = sqlite3.connect('.databases/packages.db')
            cur = db.cursor()
            cur.execute(f"INSERT INTO packages(name,dependency,author,version,last_modified,os,location,extension,privacy,message) VALUES('{self.file['init']['name']}','{self.file['dependency']}','{self.file['init']['author']}','{self.file['init']['version']}','{self.file['init']['details']['last_modified']}','{self.file['init']['details']['os']}','{self.file['init']['details']['location']}','{self.file['init']['details']['extension']}','{self.file['init']['details']['privacy']}','{self.file['init']['details']['message']}')")
            db.commit()
            db.close()
            
            #update log
            self.pfile = self.file['init']['details']['location']+'/'+self.file['init']['name']
            self.ftransfer()
            log(f"jpm: upload[{name}@jpm] [{calendar.timegm(time.gmtime())}] [success]]")         
        except:
            log(f"jpm: upload[{name}@jpm] [{calendar.timegm(time.gmtime())}] [fail]]")         
    def remove(self,name):
        self.name = name
        self.state = 'R'
        try:
            #remove data from package
            #old way of deleting specific data
            readata = json.load(open('.jpm/package.json'))
            newarr = []
            for x in readata:
                if str(x['init']['name']) != str(name):
                    newarr.append(x)
            with open('.jpm/package.json','w+') as init:
                data = json.dumps(newarr)
                init.write(data)
                
                #remove data from database
                db = sqlite3.connect('.databases/packages.db')
                cur = db.cursor()
                cur.execute(f"DELETE FROM packages WHERE name='{name}'")
                db.commit()
                db.close()
                
            #log remove file
            self.ftransfer()
            log(f"jpm: delete[{name}@jpm] [{calendar.timegm(time.gmtime())}] [success]]")         
        except:
            log(f"jpm: delete[{name}@jpm] [{calendar.timegm(time.gmtime())}] [fail]]")
    def helper():
        print("Hey")
    
"""
now?
"""
    