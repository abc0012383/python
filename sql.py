#!/usr/bin/python

import sqlite3
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

conn = sqlite3.connect('use.db')
c = conn.cursor()
cursor = c.execute("select * from issued order by rowid desc limit 1;")
for row in cursor:
    l1 = list(row)
conn.close()

l2 = [
    'time','xxx',
]

l3 = dict(zip(l2, l1))

conn = sqlite3.connect('use.db')
c = conn.cursor()
cursor1 = c.execute("select * from used order by rowid desc limit 1;")
for row1 in cursor1:
    l4 = list(row1)
conn.close()

l5 = dict(zip(l2, l4))

json.dump(l3, open('/tmp/issued.txt', 'w'))
json.dump(l5, open('/tmp/used.txt', 'w'))

with open('/tmp/issued.txt', 'r') as r:
    line = r.readlines()

with open('/tmp/issued.txt', 'w') as w:
    for k in line:
        w.write(k.replace(',', '\n'))

with open('/tmp/used.txt', 'r') as r:
    lines = r.readlines()

with open('/tmp/used.txt', 'w') as w:
    for v in lines:
        w.write(v.replace(',', '\n'))

sender = 'it@xxx.com'
receiver = 'it@xxx.com'
subject = 'test subject'
content = '<html><h1>mail with file test again</h1></html>'
smtpserver = 'xxx-com.mail.protection.outlook.com'

msgRoot = MIMEMultipart('mixed')
msgRoot['Subject'] = subject
msgRoot['From'] = sender
msgRoot['To'] = receiver

msgText = MIMEText(content, 'html', 'utf-8')
msgRoot.attach(msgText)

fp = open('/tmp/issued.txt', 'rb')
msgAtt = MIMEText(fp.read(), 'base64', 'utf-8')
msgAtt["Content-Type"] = 'application/octet-stream'
msgAtt["Content-Disposition"] = 'attachment; filename="issued.txt"'
msgRoot.attach(msgAtt)

fp1 = open('/tmp/used.txt', 'rb')
msgAtt1 = MIMEText(fp1.read(), 'base64', 'utf-8')
msgAtt1["Content-Type"] = 'application/octet-stream'
msgAtt1["Content-Disposition"] = 'attachment; filename="used.txt"'
msgRoot.attach(msgAtt1)

if __name__ == '__main__':
    smtp = smtplib.SMTP()
    smtp.connect('xxx-com.mail.protection.outlook.com')
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()


