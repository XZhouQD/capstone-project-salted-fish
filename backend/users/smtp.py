#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email(receiver_email,email_content,email_subject):
    smtp_host = "smtp.exmail.qq.com"
    smtp_user = "no-reply@mail.x-zhou.com"
    smtp_pass = "PcaVXEZo52c7ktes"
    sender = 'no-reply@mail.x-zhou.com'
    receivers = [receiver_email]
    email_message = MIMEText(email_content, 'plain')
    email_message['From'] = Header("mail.x-zhou.com")
    email_message['To'] = Header(receiver_email)

    subject = email_subject
    email_message['Subject'] = Header(subject)

    server = smtplib.SMTP_SSL(smtp_host,465)
    server.login(smtp_user,smtp_pass)
    server.sendmail(sender, receivers, email_message.as_string())

#send_email('852940804@qq.com','test email','TEST')

