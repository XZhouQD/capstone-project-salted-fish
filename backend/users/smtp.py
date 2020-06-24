#!/usr/bin/python3
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


def send_email(receiver_email,email_content,email_subject):
    smtp_host = "smtp.exmail.qq.com"
    smtp_user = "no-reply@mail.x-zhou.com"
    smtp_pass = "PcaVXEZo52c7ktes"
    sender = 'no-reply@mail.x-zhou.com'
    receivers = [receiver_email]

    email = MIMEMultipart('alternative')
    email.attach(MIMEText(email_content, 'html'))

    email_message = MIMEMultipart('related')
    email_message['From'] = Header("mail.x-zhou.com")
    email_message['To'] = Header(receiver_email)
    email_message['Subject'] = Header(email_subject)
    email_message.attach(email)

    # path/picture_name
    file = open('C:/Users/test.jpg', 'rb')
    picture = MIMEImage(file.read())
    file.close()
    picture.add_header('Content-ID', '<image1>')
    email_message.attach(picture)

    server = smtplib.SMTP_SSL(smtp_host,465)
    server.login(smtp_user,smtp_pass)
    server.sendmail(sender, receivers, email_message.as_string())

# mail_msg = """
#     <p>Python test...</p>
#     <p>Picture:</p>
#     <p><img src="cid:image1"></p>
#     """
# send_email('852940804@qq.com',mail_msg,'TEST')

