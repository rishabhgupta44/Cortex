# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import os,time

def ping_ata():
   while True:
        os.system('ping "www.google.com"')
        time.sleep(10)    
ping_ata()