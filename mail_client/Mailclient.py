import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()
server.ehlo()


with open('password.txt', 'r') as f:

	password = f.read()
	
server.login('sreeragpb0@gmail.com', 'password')

msg = MIMEMultipart()
msg['From'] = 'sreeragpb0@gmail.com'
msg['To'] = 'sreeragtb0@gmail.com'
msg['Subject'] = 'testing with python'

 
 
with open('hi.txt' , 'r') as f:
	message = f.read()
 	
msg.attach(MIMEText(message, 'plain'))



filename = 'coding.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')

text = msg.as_string()


server.sendmail('sreeragpb0@gmail.com', 'sreeragtb0@gmail.com', text)


