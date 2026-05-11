# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

from Core import BrocaArea as BrainOn
import os
import sys
from Core import Configure as configure
from . import Tasks as tasks

from subprocess import call as _

def main():
    JsonCheck = BrainOn.FileHandler.FileJsonChecker()

    # Handle None case gracefully - JsonCheck validation
    if JsonCheck is None:
        print("System initialization: Configuration check returned no result. Proceeding with default settings.")
        JsonCheck = 0
    
    if int(JsonCheck) == int(1):
        AuthJson = BrainOn.WSentence.Jauth('true')
        if AuthJson:
              PID = os.getpid()
              #_(['python3','pendrive.pyw'])
              tasks.ThisSet('Cortex',1)
              _([sys.executable,'-m','Cortex'])
              #_(['python3','JBackground.pyw']) 
           
    else:
        print("System ready. Cortex is prepared to assist you.")
        # Background initialization complete; return to main Cortex loop


if __name__ == '__main__':
    main()