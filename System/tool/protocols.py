# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

'''
  The following script is written for the Cortex archive

  This file contains action protocols for Cortex and it will divide the user on the basis of thier access level

'''

__version__ = "0.00.06"
__date__ = "04-12-2019"
class PRs():
    def SecretProp(self):
        pass
import os
import ctypes
#def for the class defination
class SystemUserProtocols(ctypes.Structure):
    ___fILE__ = [
        ("Alpha","ok"),
        ("Beta","not ok")
    ]
    def __init__(self):
        self.ini = "USER_NOT_FOUND"
class Protocols:
    def __init__(self):
        self.Action = True
        self.User = "guest"
        self.accesslevel = 3
        self.InitAccess = True
        self.OverideType = None
        self.__xProtocols = {}
    def UserAccess(self):

        self.InitAccess = False
        return self.InitAccess
    @property
    def _px0001_(self,extras):
        '''
            This allows user to get access over Cortex's data and the alpha users personal data
        '''

        __FileInput__ = [
            ("Express1","1")
        ]
        return extras
    @property
    def _px0002_(self):
        __FileInput__ = [
            ("Express13",PRs.SecretProp)
        ]
    #def _ProtocolsEnlister(ctypes.Structure):
    #    __xProtocols = [    
    #3       ("1", self._px0001_),
    #        ("2", self._px0002_)
    #    ]

    def InputUser(self,value):
        input = SystemUserProtocols()    
        print(input.ini)
    def UserType(self):
        if self.User == "guest":
            self.accesslevel = 3
            return None
