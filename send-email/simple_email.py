import yagmail
import os
sender = "whelan.eoin69@gmail.com"
receiver = "whelan.eoin6@gmail.com"

subject = "This is the subject"
contents = """
Here is the content of my email
spread out over multiple\n\n
lines
"""
#email = os.getenv("PYTHON_EMAIL")
#password = os.getenv("PYTHON_EMAIL_PASSWORD")
#print(email, password)


yag = yagmail.SMTP(user=sender, password=os.getenv("PYTHON_EMAIL_PASSWORD"))
yag.send(to=receiver, subject=subject, contents=contents)




