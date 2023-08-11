#========== Author : Sayed Mujtaba Ahmady =================================
# Facebook Page : https://www.facebook.com/profile.php?id=100075938127515 +
# Instagram Page : https://www.instagram.com/_tech.box/                   +
# Youtube : https://www.youtube.com/@techbox8186                          +
# Github : https://github.com/ahmadysayed                                 + 
#==========================================================================
#Never forget to read the comments 

# ===========================================================================
# Usage:
#     For runnig this script you need to install python3

#     Don't forget to install the wtilio module

#     pip install twilio

# For Runing the code:
#     you need to open your terminal or cmd in same folder as script and run
#     ==================================
#     +         python3 sms.py         + 
#     ==================================

#     Go throw website and make account then read the documentation to understand more
#     https://www.twilio.com/


from twilio.rest import Client

account_sid = 'AC7f2dd525a3aa20fb3dcc68a7c095c5f0'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+13135138585',
  body='Leave your feedback',
  to='+33667372598'
)

print(message.sid)