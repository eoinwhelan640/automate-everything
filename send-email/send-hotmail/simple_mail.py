import smtplib
import os

sender = "someemail@hotmail.com"
receiver = "whelan.eoin6@gmail.com"
password = os.getenv("SOMEPASSWORD")


# Huge difference, the subject is in body of email now! The lib parses it out when sending
body = """\
Subject: Hello hello

Body of email - note how subject is in here too
"""

if __name__ == "__main__":
    server = smtplib.SMTP("smtp.office365.com", 587) # (domain[of outlook], port)
    server.starttls() # start tls protocol which is protocol for sending email in encrypted form
    server.login(sender, password=password) # login into our email account
    server.sendmail(sender, receiver, body)
    server.quit()