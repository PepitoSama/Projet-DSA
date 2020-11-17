import os
import csv

maildir = os.getcwd() + '/maildir'
dirNameArray = os.listdir(maildir)

with open('output.csv','w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writeheader(["_T","_F","_S","_D"])

for dirName in dirNameArray :
    try :
        emailList = os.listdir(maildir + '/' + dirName + '/inbox')
        for email in emailList :
            print(email)
    except:
        print("No Inbox for " + dirName)