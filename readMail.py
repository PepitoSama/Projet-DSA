# Import the email modules we'll need
from email.parser import BytesParser, Parser
from email.policy import default
from email.message import EmailMessage
import email
import csv

def readAndWriteRow(path,writer):

    # If the e-mail headers are in a file, uncomment these two lines:
    with open(path, 'r') as fp:
        msg_str = fp.read()
        headers = email.message_from_string(msg_str)
        msg = email.message_from_string(msg_str).get_payload()
        fp.close()

        # write in csv
        writer.writerow([headers['To'],headers['From'],headers['Subject'],headers['Date'],msg])

# print('Content : ' + msg)
