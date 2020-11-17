# Import the email modules we'll need
from email.parser import BytesParser, Parser
from email.policy import default
from email.message import EmailMessage
import email

# If the e-mail headers are in a file, uncomment these two lines:
with open("1.", 'r') as fp:
    msg_str = fp.read()
    headers = email.message_from_string(msg_str)
    msg = email.message_from_string(msg_str).get_payload()
    fp.close()

print('To: {}'.format(headers['To']))
print('From: {}'.format(headers['From']))
print('Subject: {}'.format(headers['Subject']))
print('Date : {}'.format(headers['Date']))
# print('Content : ' + msg)
