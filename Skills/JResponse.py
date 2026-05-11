# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import string
import os
import json
import random
from Core import Configure as configure
from Core import BrocaArea as JBrain
from Security import Decrypt as DecryptModule
Decryptor = DecryptModule.decryptor

class JResponse:
    pass