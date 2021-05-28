
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email_id = 'shuaibdollie36@gmail.com'
receiver_email_id = 'vandiemennahum@gmail.com,jasoncee017@gmail.com,thapelo@lifechoices.co.za'
password = input("Enter your password")
subject="Greetings"
msg=MIMEMultipart()
msg['From']=sender_email_id
msg['To']=receiver_email_id
msg['Subject']=subject
body = "hi guys how are you. i am doing fine\n"
body = body + "How was your task yesterday"
msg.attach(MIMEText(body, 'plain'))
text=msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login(sender_email_id, password)
# message to be sent

# sending the mail
s.sendmail(sender_email_id, receiver_email_id, text)
# terminating the session
s.quit()