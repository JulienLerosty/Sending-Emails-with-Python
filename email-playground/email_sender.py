import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Julien Lerosty'
email['to'] = 'julien.lerosty@gmail.com'
email['subject'] = 'You won 1M $'

email.set_content(html.substitute({'name': 'Tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('julien.lerosty@gmail.com', 'jyzo qmsx fkqy pxpy')
  smtp.send_message(email)
  print('all good boss')
