import gettext
import os
'''
   This module contains the data and setback message for usage
'''
_ = gettext.gettext
#sccript imported
SETUP_EX_USE = _("This script is not in use")
#script using __main__
SETUP_INIT_USE = _("Setup main use")
#unauthorised script
ACCESS_DENIED = _("Acess Denied")

_MessageLibrary = {

    1 : SETUP_EX_USE,
    2 : SETUP_INIT_USE,
    3 : ACCESS_DENIED 
}

def message(code):
    print(_MessageLibrary[code])

message(3)
 