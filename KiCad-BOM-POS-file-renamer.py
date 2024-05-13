# Program to convert the BOM, bottom-pos and top-pos files generated by KiCad to JLCPCB compatible files,
# (see: https://jlcpcb.com/help/article/81-How-to-generate-the-BOM-and-Centroid-file-from-KiCAD).

# Input file names must begin with the KiCad Project Name and be suffixed in a particular way.
# The table below shows the expected input suffix and the produced output file suffix upon successfull conversion:

# Filetype              +   Input Suffix        +   Output Suffix
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# BOM                  +   -BOM.csv            +   -JLC-BOM.csv
# Top Position File    +   -top-pos.csv        +   -top-CPL.csv
# Bottom Position File +   -bottom-pos.csv     +   -bottom-CPL.csv          

import pandas as pd

def is_not_blank(s):
    # Function to check if a string does not mearly consist of spaces.
    # Source: https://stackoverflow.com/a/27982561
    return bool(s and not s.isspace())

def reoder_and_rename_columns(src_filename, target_filename, column_order, replacement_line):
    df = pd.read_csv(src_filename)
    df_reorder = df[column_order] # Rearrange the columns
    df_reorder.columns = replacement_line # Rename the columns
    df_reorder.to_csv(target_filename, index=False)

# Configuration:
WorkingDirectory = '' # Add folder path when running the program from a nested folder.
BOMOrder = ['Value', 'Reference', 'Footprint', 'LCSC'] # Column names order, in terms of KiCad BOM column names.
BOMReplacementLine = ['Comment', 'Designator', 'Footprint', 'LCSC Part Number'] # BOM output header.
CPLOrder = ['Ref', 'Val', 'Package', 'PosX', 'PosY', 'Rot', 'Side'] # Column names, in terms of KiCad CPL column names. Order stays the same.
CPLReplacementLine = ['Designator', 'Val', 'Package', 'Mid X', 'Mid Y', 'Rotation', 'Layer'] # CPL output header.

# REPL Logic:
ValidInput = False

while (ValidInput == False):
    KiCadProjectName = input('Enter KiCad Project Name: ') 
    if(is_not_blank(KiCadProjectName)):
        ValidInput = True
    else:
        print('Project Name can not be empty, try again.')

ValidInput = False

while (ValidInput == False):
    BOMOptions = input('BOM Y/N?: ')
    if(BOMOptions == 'Y' or BOMOptions == 'y' or BOMOptions == 'N' or BOMOptions == 'n'):
        ValidInput = True
    else:
        print('Invalid input, try again.')

ValidInput = False

while (ValidInput == False):
    CPLOptions = input('CPL Y/N?: ')
    if(CPLOptions == 'Y' or CPLOptions == 'y' or CPLOptions == 'N' or CPLOptions == 'n'):
        ValidInput = True
    else:
        print('Invalid input, try again.')

ValidInput = False

if(CPLOptions == 'Y' or CPLOptions == 'y'):
    while (ValidInput == False):
        CPLType = input('CPL top/bottom/both?: ')
        if(CPLType == 'top' or CPLType == 'bottom' or CPLType == 'both'):
            ValidInput = True
        else:
            print('Invalid input, try again')
else:
    pass

# Convert the files according to the selected options:
if(BOMOptions == 'Y' or BOMOptions == 'y'):
    reoder_and_rename_columns((WorkingDirectory + KiCadProjectName + '-BOM.csv'), (WorkingDirectory + KiCadProjectName + '-JLC-BOM.csv'), BOMOrder, BOMReplacementLine)
else:
    pass

if(CPLOptions == 'Y' or CPLOptions == 'y'):
    if (CPLType == 'top' or CPLType == 'both'):
        reoder_and_rename_columns((WorkingDirectory + KiCadProjectName + '-top-pos.csv'), (WorkingDirectory + KiCadProjectName + '-top-CPL.csv'), CPLOrder, CPLReplacementLine)
    else: 
        pass 
    if (CPLType == 'bottom' or CPLType == 'both'):
        reoder_and_rename_columns((WorkingDirectory + KiCadProjectName + '-bottom-pos.csv'), (WorkingDirectory + KiCadProjectName + '-bottom-CPL.csv'), CPLOrder, CPLReplacementLine)
    else: 
        pass 
else:
    pass
