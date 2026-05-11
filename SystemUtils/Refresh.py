# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import os
import importlib
from Skills import Text as text
from Core import BrocaArea as broca_area
import CodeReac as code_reac
from Core import Response as response
from Skills import Action as action
from Core import Configure as configure
from Core import CortexModule as Cortex_module
from SystemUtils import Tasks as tasks
module = [broca_area, code_reac, response, action,
          configure, Cortex_module, tasks]


def refresh():
    for x in module:
        importlib.reload(x)

'''
def restart():
    from win32com.client import GetObject
    configure.j_re_reset()
    os.system('start Main')
    WMI = GetObject('winmgmts:')
    processes = WMI.InstancesOf('Win32_Process')

    for p in WMI.ExecQuery('select * from Win32_Process where Name="cmd.exe"'):
        os.system("taskkill /pid "+str(p.Properties_('ProcessId').Value))
'''