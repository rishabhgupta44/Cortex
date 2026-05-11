
import os,json,sys
import message
def AllElementCheck(word):
    pass
class Dictionary(object):

    def __init__(
        self,
        casesensitive = False,
        lang='EN',
        TYPE='str'
        ):
          
        self.dictionary = []
        self.lang = lang  # EN BY DEFAULT
        self.type = TYPE
        self.SENSITIVITY = casesensitive

    @property
    def GET_DICTIONARY(self):
        if self.lang == 'EN':
            with open('/Brain/FrontalLobe/words/all.json') as WordArray:
                self.dictionary = json.load(WordArray)
                return self.dictionary
if __name__=='__main__':
   message.message(1)
else:
    message.message(2)
filename = ''
