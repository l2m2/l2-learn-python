import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders

config = {
  'host': '10.4.1.44',
  'port': 9281,
  'user': 'top-sysadmin@xxx.com',
  'password': 'top-xxx.2017',
  'from': 'top-sysadmin@xxx.com',
  'to': 'leon.li@xxx.com'
}

if __name__ == "__main__":
  smtp = smtplib.SMTP(config['host'], config['port'])
  smtp.set_debuglevel(2)
  smtp.starttls()
  smtp.login(config['user'], config['password'])
  message = MIMEMultipart()
  message['Subject'] = Header('Python Mail StartTLS Test', 'utf-8')
  message['From'] = config['from']
  message['To'] = config['to']
  message.attach(MIMEText('Test Content'))
  smtp.sendmail(
    config['user'], 
    config['to'],
    message.as_string()
  )
  smtp.quit()