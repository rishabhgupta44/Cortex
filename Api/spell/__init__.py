'''

 This file is a basic version of spell checker based purely on the percentage of compatibility of the word and the letters init
 This script is written for the Cortex archive 
 Reanalysing of the script in c++ language

'''

import json
import os

import message
import words

__version__ = '0.0.1'  # first version
__label__ = 'SpellCheck'
__engine__ = 'Cortex'  # used for
__last__ = '13-12-2019'  # last update


class SpellCheck():

    def __init__(
        self,
        word,
        lang='EN',
        type='US',
        buffer=2,
        FlawSense=None,
        frequncy=None
    ):

        self.word = (word).lower()
        WordCollection = words.Dictionary()
        self.wordcache = WordCollection.GET_DICTIONARY
        self.lang = 'EN'  # By default
        self.area = 'US'  # as i don't have an english accent
        self.correct = False  # by default
        self.req = True  # requirement of correction is alway enabled but false in some cases
        self.buffer = buffer  # it is the word correction pattern
        # flaw sense mainly deals with the extra letter in word unralated to the word at all
        self.flaw = FlawSense
        self.contency = frequncy  # frequency of the word list
        self.letter = int(len(word))
        self.data = json.load(open(os.path.join("Brain/FrontalLobe/words/"+"all.json")))
        ''''
             |             /
             |            / 
             |           /  
             |   _______/   
             |  /    
             | /.
             |/_____________        
        
             WORD LIST MANAGER
        '''
    def randcheck(self):

        if self.word in self.data: self.correct = True
        else: self.correct = False
    '''
        I will make the project mainly based on the mistakes i make while typing which are:

        -> Skipping a letter in a word

    '''

    def skipcorrection(self):
        '''
                \   /
                 \ /
                 / \
                /   \
           Make a array of all the words starting with the provided letter or the present of the letter init
           In order to check the correction of the word in the area I need to first 
        '''
        pass

