import broca_area as Brain
import text,tasks,os

try:
    text.Notice('Starting pendrive Services',5)
    tasks.ThisSet('PendriveBackup',1)
    i=0
    ReadAccess = False
    while i==0:
        PendriveCheck = Brain.FileHandler.PenChecker
        if PendriveCheck:
            ReturnType = Brain.FileHandler.PenDriveBackup()
            if ReturnType:
                tasks.ThisSet('PendriveBackup',0)
                ReadAccess = True
                i=1
            if not ReturnType:
                i=0
    if ReadAccess:
       text.Notice('File uploaded to the pendrive',5)
except:
    text.Notice('Error in uploading the files in the document',6)
    tasks.ThisSet('PendriveBackup',0)
