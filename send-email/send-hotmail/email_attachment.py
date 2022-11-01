import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

sender = 'someemail@outlook.com'
receiver = '@gmail.com'
password = os.getenv("SOME_ENV_VAR")

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Hello again!'


body = """
<h2>Hi there!</h2>
There are only two cats flying today!
Let's hope for more!
"""

mimetext = MIMEText(body, 'html')
message.attach(mimetext)


attachment_path = "image_attach.jpg"
# We create an attachment file to use later.
# use rb mode because we're creating a python file object
attachment_file = open(attachment_path, "rb")
payload = MIMEBase('application', 'octate-stream')
payload.set_payload(attachment_file.read()) # the content of the image in binary mode
encoders.encode_base64(payload)
# filename arg controls what the attachment is called in the mail, otherwise its randomly generated
payload.add_header("Content-Disposition", "attachment", filename=attachment_path)
message.attach(payload)


if __name__ == "_main__":
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(sender, password)
    message_text = message.as_string()
    print(message_text)
    server.sendmail(sender, receiver, message_text)
    server.quit()