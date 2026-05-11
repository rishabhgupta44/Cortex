# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

#!usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from Core import CortexModule as jModule
from Core import BrocaArea as Brain
from Core.Configure import greetings, nameDes
from SystemUtils import Background

if __name__ == '__main__':
    Jauth = Brain.CSentence.Jauth()

    if Jauth == 'false':
       subprocess.call([sys.executable, '-m', 'SystemUtils.Background'])
    
    nameDes()
    while True:
        vr = jModule.Cortex()
        if vr == 1:
            break
