#!/usr/bin/env python
# coding: utf-8

# In[13]:


import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = 'New Albums This Week - email automation test-take 2'
body = 'This is a test for the email informing you of the new albums released this week./n Meant to test automation and send this automatically in the morning.'
sender_email = 'ed.doris@gmail.com'
receiver_email = 'braedenlynn@gmail.com'
password = 'dqmptmojjxazrixo'

email = MIMEMultipart()
email["From"] = sender_email
email["To"] = receiver_email 
email["Subject"] = subject

email.attach(MIMEText(body, "plain"))
# attach_file = open(file, "rb") # open the file
# report = MIMEBase("application", "octate-stream")
# report.set_payload((attach_file).read())
# encoders.encode_base64(report)
# #add report header with the file name
# report.add_header("Content-Decomposition", "attachment", filename = file)
# email.attach(report)

session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_email, password) #login with mail_id and password
text = email.as_string()
session.sendmail(sender_email, receiver_email, text)
session.quit()
print('Mail Sent')


# In[ ]:




