#Sending Emails

import smtplib       # used to connect to the email server and send emails
import getpass       #used to securely input the email password
from email.mime.text import MIMEText          #used to create the email content

def send_email():
    sender_address = 'sahajwanisoham2707@gmail.com'
    password = getpass.getpass()
    subject = 'Machine Learning'
    msg = '''
          Hi everyone!
          I am Soham Sahajwani.
    '''
    #server initialisation
    server = smtplib.SMTP('smtp.gmail.com',587)     # 587- default port number of SMTP #lhkqcezwozlpoqzd
    server.starttls()
    server.login(sender_address,password)
    
    #draft my message body
    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = sender_address
    msg['To'] = 'sohamsahajwani2707@gmail.com'
    recipients = 'sohamsahajwani2707@gmail.com'
    #recipients = ['___@gmail.com' , '____@gmail.com' , '____@gmail.com'] - for multiple recipients
    
    #msg.set_param('importance','high value')
    
    server.sendmail(sender_address,recipients,msg.as_string())
    
send_email()
