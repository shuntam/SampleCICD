from smtplib import SMTP
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import smtplib
import os

mail_list='shubha.srinivasan@nielsen.com'
send_from='voz_daily_production@nielsentam.com.au'
message="File Not Present"
msg = MIMEMultipart()
msg['From'] = send_from
msg['To'] = mail_list
msg['Date'] = '20200521'
msg['Subject'] = "STVM Demoevent file"
msg.attach(MIMEText(message))

smtpObj = smtplib.SMTP('mail.agbnielsen.com.au')
#with SMTP("mail.agbnielsen.com.au") as smtp:
filename = "\\10.130.41.150\VPMlinkages\stvm_demoevent302_20200524.csv"
if not os.path.exists(filename) :
    smtpObj.sendmail(send_from, mail_list, msg.as_string())      
#else :       
