import yagmail
import os
import time
import datetime as dt

sender = "whelan.eoin69@gmail.com"
receiver = "whelan.eoin6@gmail.com"

subject = "This is the scheduled email subject"
contents = """
Here is the content of my scheduled email
spread out over multiple\n\n
lines
"""

# Stupid way to loop, surely a timer library exists
if __name__=="__main__":
    while True:
        now = dt.datetime.now()
        if now.hour == 13 and now.minute == 15:
            yag = yagmail.SMTP(user=sender, password=os.getenv("PYTHON_EMAIL_PASSWORD"))
            yag.send(to=receiver, subject=subject, contents=contents)
            print("EMAIL SENT")
            time.sleep(60)




