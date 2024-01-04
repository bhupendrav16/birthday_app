import os 
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

def send_message(receiver,name):

    load_dotenv()
    s = "bhupendra.v.brudite@gmail.com"
    p = os.environ.get('EMAIL_PASS')
    r = receiver

    sub = "Special Day"

    body= """
    happy birthday
    """
    em = EmailMessage()
    em['From']= s 
    em['To'] = r
    em['Subject'] = sub 
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(s,p)
        smtp.sendmail(s,r,em.as_string())
        