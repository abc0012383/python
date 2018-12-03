import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


f=open('/root/nioj','rb')
fp=f.readlines()
sender = 'xxx@xxx.com'
receiver = 'xxx@xxx.com'
subject = 'Domain Password Expire Check'
content = 'These users domain password will expire within 10 days %s' %(fp)
smtpserver = 'xxx-com.mail.protection.outlook.com'

msgRoot = MIMEMultipart('mixed')
msgRoot['Subject'] = subject
msgRoot['From'] = sender
msgRoot['To'] = receiver

msgText = MIMEText(content, 'html', 'utf-8')
msgRoot.attach(msgText)
f.close()

if __name__ == '__main__':
    smtp = smtplib.SMTP()
    smtp.connect('xxx-com.mail.protection.outlook.com')
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()
