import urllib2
response = urllib2.urlopen('http://nwp.imd.gov.in/ts/data.php')
buf = response.read()
buf = buf.split('/><marker')
flag = False
txt = ''
for item in buf:
 itm = item.split()
 for val in itm:
  if 'BHATINDA' in val:
   item = item.split('=')
   for val in item:
    if '"F/C' in val:
     txt = txt+val[:-3]+'\n'
    elif '"Warning' in val:
     txt = txt+val[:-3]+'\n'
    elif '"2020' in val and not flag:
     txt =txt+'Issued IST:'+val[:-3]+'\n'
     flag = True
    elif '"2020' in val and flag:
     txt = txt+'Valid IST:'+val[:-3]
     flag = False
print txt
'''
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

msg = MIMEText(txt)

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Warning for Bhatinda'
msg['From'] = 'dulal.chakrabarti@gmail.com'
msg['To'] = 'dulal.chakrabarti@gmail.com'

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()
'''
