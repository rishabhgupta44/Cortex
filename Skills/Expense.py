# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import string
import json
import os
import openpyxl
import datetime

while True:

    MainIn = input('[Y/y]> ')
    if MainIn.lower() == 'y':
        Today = str(datetime.date.today())
        item = input("ITEM> ")
        cost = input("COST> ")
        wb = openpyxl.load_workbook("Cortex.xlsx")
        sheet = wb.get_sheet_by_name('EXPENSE')
        AIndex = len(sheet['A'])+1
        sheet[f'A{AIndex}'] = Today
        sheet[f'B{AIndex}'] = item
        sheet[f'C{AIndex}'] = cost

        wb.save("Cortex.xlsx")
    if MainIn.lower() != 'y':
        break
