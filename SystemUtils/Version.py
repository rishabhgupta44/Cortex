# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import CortexSelf as J
j = J.Cortex()
about = j.about()
while True:
    print(about)
    intake = input()
    if intake == '':
       break
