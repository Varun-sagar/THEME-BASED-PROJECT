import smtplib
import csv
import email
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders






def make_mail(email):
    fromaddr = "varuntejasagar016@gmail.com"
    toaddr = email

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "greetings"

    body = "welcome,good afternoon--------Thanks for registering!"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "sagar016")
    text = msg.as_string()

    server.sendmail(fromaddr, toaddr, text)
    server.quit()
   



























'''

csvreader = csv.reader(open("/home/varun/Downloads/contacts1.csv"))

for row in csvreader:
    fromaddr = "varuntejasagar016@gmail.com"
    toaddr = row[2]

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "greetings"

    body = "welcome,good afternoon"+"   "+row[0]+ "  "+row[1]

    msg.attach(MIMEText(body, 'plain'))

    filename = "letter.txt"
    attachment = open("letter.txt", "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "sagar016")
    text = msg.as_string()

    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    time.sleep(1)
'''
