import smtplib
import sendgrid as sg
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
SUBJECT = "chikkanam"
s = smtplib.SMTP('smtp.gmail.com', 587)

def sendmail(TEXT,email):
    print("sorry we cant process your candidature")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    # s.login("il.priyakumaran3112@gmail.com", "lovemuffin123")
    s.login("priyakumaran3112@gmail.com", "lovemuffin123")
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    # s.sendmail("il.priyakumaran3112@gmail.com", email, message)
    s.sendmail("il.priyakumaran3112@gmail.com", email, message)
    s.quit()
def sendgridmail(user,TEXT):
  
    # from_email = Email("priyakumaran3112@gmail.com")
    from_email = Email("priyakumaran3112@gmail.com") 
    to_email = To(user) 
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain",TEXT)
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()
    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)
