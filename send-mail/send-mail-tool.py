import sys
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders
import argparse
import json

def send_mail(host, port, user, password, from_, to, cc, bcc, subject, content, attachments):
  smtp = smtplib.SMTP(host, port)
  smtp.set_debuglevel(1)
  smtp.starttls()
  smtp.login(user, password)
  message = MIMEMultipart()
  message['Subject'] = Header(subject, 'utf-8')
  message['From'] = from_
  message['To'] = ','.join(to)
  if cc:
    message['Cc'] = ','.join(cc)
  if bcc:
    message['Bcc'] = ','.join(bcc)
  message.attach(MIMEText(content, 'html', 'utf-8'))
  for a in attachments:
    if not os.path.isfile(a):
      continue
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(a, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename=('gbk', '', os.path.basename(a)))
    message.attach(part)
  smtp.sendmail(
    from_,
    to + cc + bcc,
    message.as_string()
  )
  smtp.quit()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Send Mail Parser')
  parser.add_argument('--host', type=str, required=True)
  parser.add_argument('--port', type=str, required=True)
  parser.add_argument('--user', type=str, required=True)
  parser.add_argument('--password', type=str, required=True)
  parser.add_argument('--from', type=str, required=True)
  parser.add_argument('--to', type=str, required=True)
  parser.add_argument('--cc', type=str, required=False)
  parser.add_argument('--bcc', type=str, required=False)
  parser.add_argument('--subject', type=str, required=True)
  parser.add_argument('--content', type=str, required=True)
  parser.add_argument('--attachments', type=str, required=False)
  args = vars(parser.parse_args())
  to = [x.strip() for x in args['to'].split(';') if x.strip() != '']
  cc = []
  if args['cc']:
    cc = [x.strip() for x in args['cc'].split(';') if x.strip() != '']
  bcc = []
  if args['bcc']:
    bcc = [x.strip() for x in args['bcc'].split(';') if x.strip() != '']
  subject = args['subject']
  content = args['content']
  attachments = []
  if args['attachments']:
    attachments = [x.strip() for x in args['attachments'].split(';') if x.strip() != '']
  send_mail(args['host'], args['port'], args['user'], 
    args['password'], args['from'], to, cc, bcc, subject, content, attachments)
