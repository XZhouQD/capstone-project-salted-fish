#!/usr/bin/python3
import smtplib, yaml
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

class SMTP:
    def __init__(self):
        f = open('smtp.config', 'r', encoding='utf-8')
        config = yaml.load(f.read(), Loader=yaml.FullLoader)
        smtp_host = config['SMTP']['Host']
        smtp_port = int(config['SMTP']['Port'])
        self.smtp_user = config['SMTP']['User']
        self.smtp_pass = config['SMTP']['Pass']
        self.sender = config['SMTP']['Sender']
        self.server = smtplib.SMTP_SSL(smtp_host, smtp_port)
        self.server.login(self.smtp_user, self.smtp_pass)

    def send_email_plain(self, receiver, content, subject):
        message = MIMEText(content, 'plain', 'utf-8')
        return self.send_out(receiver, subject, message)

    def send_email_html(self, receiver, content, subject):
        message = MIMEText(content, 'html', 'utf-8')
        return self.send_out(receiver, subject, message)

    def send_out(self, receiver, subject, message):
        message['From'] = Header(self.sender)
        message['To'] = Header(receiver)
        message['Subject'] = Header(subject)
        try:
            self.server.sendmail(self.sender, receiver, message.as_string())
            print("Email send to " + str(receiver) + " success")
            return True
        except smtplib.SMTPException(e):
            print(f"Send email to {str(receiver)} failed")
            print(repr(e))
            return False

'''
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
'''

# mail_msg = """
#     <p>Python test...</p>
#     <p>Picture:</p>
#     <p><img src="cid:image1"></p>
#     """
# send_email('852940804@qq.com',mail_msg,'TEST')

