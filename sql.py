#!/usr/bin/env python

import sqlite3
import smtplib
from pyecharts import Bar
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

conn = sqlite3.connect('/opt/licences/licence_check/use.db')
c = conn.cursor()
cursor = c.execute("select * from issued order by rowid desc limit 1;")
for row in cursor:
    issued_last_record = list(row)
conn.close()

conn = sqlite3.connect('/opt/licences/licence_check/use.db')
c = conn.cursor()
cursor1 = c.execute("select * from issued")
col_name_list = [tuple[0] for tuple in c.description]
conn.close()

conn = sqlite3.connect('/opt/licences/licence_check/use.db')
c = conn.cursor()
cursor2 = c.execute("select * from used order by rowid desc limit 1;")
for row1 in cursor2:
    used_last_record = list(row1)
conn.close()

issued_last_record.pop(0)
col_name_list.pop(0)
used_last_record.pop(0)

attr = col_name_list
value1 = issued_last_record
value2 = used_last_record
bar = Bar("Bar chart", "Licences usage status in licences server")
bar.add("issued licences", attr, value1, mark_line=["average"], mark_point=["max", "min"], is_label_show=True,
        is_datazoom_show=True)
bar.add("used licences", attr, value2, mark_line=["average"], mark_point=["max", "min"], is_label_show=True,
        is_datazoom_show=True)
bar.render()

sender = 'it@xxx.com'
receiver = 'it@xxx.com'
subject = 'Licences Check'
content = '<html><h1>Licences usage status in licences server</h1></html>'
smtpserver = 'xxx-com.mail.protection.outlook.com'

msgRoot = MIMEMultipart('mixed')
msgRoot['Subject'] = subject
msgRoot['From'] = sender
msgRoot['To'] = receiver

msgText = MIMEText(content, 'html', 'utf-8')
msgRoot.attach(msgText)

fp = open('render.html', 'rb')
msgAtt = MIMEText(fp.read(), 'base64', 'utf-8')
msgAtt["Content-Type"] = 'application/octet-stream'
msgAtt["Content-Disposition"] = 'attachment; filename="licences_check.html"'
msgRoot.attach(msgAtt)

if __name__ == '__main__':
    smtp = smtplib.SMTP()
    smtp.connect('xxx-com.mail.protection.outlook.com')
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()

