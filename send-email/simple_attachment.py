import yagmail
import os

sender = "whelan.eoin69@gmail.com"
receiver = "whelan.eoin6@gmail.com"
# When using attachments, you use the content as a list rather than a simple string of text
# We provide the path to the attachment and yagmail lib will handle attaching
contents = ["Sample email with an attachment", "sample_attachment.txt"]
subject = "Test file attachments"

if __name__ == "__main__":
    yag = yagmail.SMTP(user=sender, password=os.getenv("PYTHON_EMAIL_PASSWORD"))
    yag.send(to=receiver, subject=subject, contents=contents)
    print(f"EMAIL SENT")