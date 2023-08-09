import smtplib
from email.message import EmailMessage 
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Mujtaba Ahmady'
email['to'] = 'Type the receiver email'
email['subject'] = 'Subscribe for Updates'


email.set_content(html.substitute({'name' : "Mujtaba"}), 'html')

# You can change this base on you server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # the following commands login to your account and then send the email but in the second field you need to type your 
    # password if you write your usual password it will give you error because due to security reason it is not possible to 
    # login so you need to config app password so search on google that how you can generate an app password 
    smtp.login('Sender Email', 'App Configuration Password') 
    smtp.send_message(email)
    print('all good sir!')