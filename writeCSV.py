import os
import csv
import readMail

maildir = os.getcwd() + '/testDir'
dirNameArray = os.listdir(maildir)


def writeHeader():
    with open('output.csv','w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["_T","_F","_S","_D","content"])


def getAllpath():
    res = []
    for userDir in getUserDirArray():
        res.append(getAllMailUserDir(userDir))
    return res

def getUserDirArray():
    return os.listdir(maildir)

def getAllMailUserDir(userDir):
    inboxPath = maildir + '/' + userDir + '/inbox'
    currentDirContent = os.listdir(inboxPath)
    Browse(currentDirContent,inboxPath)

def Browse(dir,currentDir):
    # cas vide
    if(len(dir) == 0):
        return []
    #cas ou c'est un fichier
    [head, *tail] = dir
    print(head)
    print(tail)
    print(len(dir))
    print(type(dir))
    if(isMail(head)):
        return Browse(tail,currentDir).append(head)
    #cas c'est un répertoire
    if(not isMail(head)):
        nextDir = os.listdir(currentDir + '/' + head)
        return Browse(nextDir,currentDir)

def isMail(file):
    return file[len(file) - 1] == '_'
