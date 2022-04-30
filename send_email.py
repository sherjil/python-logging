import smtplib

from email.message import EmailMessage

msg = EmailMessage()
msg.set_content('Email sending example using Python. wow Its Simple Text Message')

fromEmail = 'from@email.com'
toEmail = 'to@email.com'

msg['Subject'] = 'Simple Text 3 Message'
msg['From'] = fromEmail
msg['To'] = toEmail
msg['Bcc'] = 'bbc@email.com'


s = smtplib.SMTP('gator4016.hostgator.com', 587)

s.starttls()

s.login(fromEmail, 'Password')
s.send_message(msg)
s.quit()
