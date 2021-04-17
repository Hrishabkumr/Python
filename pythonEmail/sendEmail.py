import smtplib
import getpass

smtp_obj = smtplib.SMTP('smtp.gmail.com',587)
print(smtp_obj.ehlo())
print(smtp_obj.starttls())

email = getpass.getpass('Email : ')
password = getpass.getpass('Password : ')
smtp_obj.login(email, password)

from_address = email
to_address = email
subject = input('enter the subject line : ')
message  = input('enter the body message : ')
msg = "Subject: "+subject+"\n"+message   #this is the standard format
success = smtp_obj.sendmail(from_address, to_address, msg)

if success=={}:
    print('Mail Sent Successfully!!!')
else:
    print('Some Error Occurred!!!')

smtp_obj.quit()