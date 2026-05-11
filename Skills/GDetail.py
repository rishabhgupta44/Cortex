# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

# Writing to an excel  
# sheet using Python 
import openpyxl,datetime
Today = str(datetime.date.today())
Weight = input("WEIGHT> ")

wb = openpyxl.load_workbook("Cortex.xlsx")
sheet=wb.get_sheet_by_name('BM')
AIndex = len(sheet['A'])+1
sheet[f'A{AIndex}'] = Today
sheet[f'B{AIndex}'] = Weight

wb.save("Cortex.xlsx")
