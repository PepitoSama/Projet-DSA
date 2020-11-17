import os

maildir = os.getcwd() + '/maildir'
dirNameArray = os.listdir(maildir)

for dirName in dirNameArray :
    try :
        emailList = os.listdir(maildir + '/' + dirName + '/inbox')
        for email in emailList :
            print(email)
    except:
        print("No Inbox for " + dirName)