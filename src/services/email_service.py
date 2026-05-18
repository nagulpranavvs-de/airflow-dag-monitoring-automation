import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class EmailService:
 def __init__(self, sender,password): self.sender=sender; self.password=password
 def send_email(self, recipient, subject, html_body):
  msg=MIMEMultipart(); msg['From']=self.sender; msg['To']=recipient; msg['Subject']=subject; msg.attach(MIMEText(html_body,'html'))
  with smtplib.SMTP('smtp.gmail.com',587) as server:
   server.starttls(); server.login(self.sender,self.password); server.send_message(msg)
