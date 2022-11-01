import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

#  MIME - Multi-purpose Internet Mail Extensions, a standard for sending emails
# MIMEMultipart is used to send text and other chars and attachments through emails
# so it lets us send an email with different parts


sender = 'someemail@outlook.com'
receiver = '@gmail.com'
password = os.getenv("SOME_ENV_VAR")

# message basically takes the form of a dictionary now, where it has keys
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Hello again!'

# the body is not a key, it is a separate component
body = """
<h2>Hi there!</h2>
There are only two cats flying today!
Let's hope for more!
"""
# We can write html in here then and MIMEText tells it to interpret as html when sending
# if left it as plain text it wouldnt interpret it at time of sending
mimetext = MIMEText(body, 'html')
# Attach expects a MIMEText type object
message.attach(mimetext)

# If you were to print it, the whole text looks like an outlook email, so it obviously gets parsed
# and understood so it can be sent in matching format
#print(message)

if __name__ == "_main__":
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(sender, password)
    message_text = message.as_string()
    print(message_text)
    server.sendmail(sender, receiver, message_text)
    server.quit()