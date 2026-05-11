# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import os,json,sys
#JTID ranges from 1 to 3220
def Notice(message,time):
    from plyer import notification

    notification.notify(
        title='Cortex',
        message=message,
        app_name='Cortex',
        app_icon='Cortex.ico',  # e.g. 'C:\icon_32x32.ico'
        timeout=time  # seconds
    )
