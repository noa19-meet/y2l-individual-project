import smtplib
from databases import *

def send_mail(email):
	
	gmail_user = 'bilblock4@gmail.com'  
	gmail_password = 'bilblock123'

	password = session.query(User).filter_by(email=email).first()
	password = password.password
	sent_from = gmail_user  
	to = [email]
	subject = 'YOUR PASSWORD'  
	body = "Your password is:" + password

	email_text = """
	From: %s  
	To: %s  
	Subject: %s

	%s
	""" % (sent_from, ", ".join(to), subject, body)

	try:  
	    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	    server.ehlo()
	    server.login(gmail_user, gmail_password)
	    server.sendmail(sent_from, to, email_text)
	    server.close()

	    print('Email sent!')
	except:  
	    print('Something went wrong...')

