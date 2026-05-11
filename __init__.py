# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import ctypes
import system.tool.protocols as P
m = P.Protocols
z = m.UserAccess
print(z)
class PStructure():
    _fields_ = [
            ("dx","Hi")
    ]
    
k = PStructure()
print(k.dx)
