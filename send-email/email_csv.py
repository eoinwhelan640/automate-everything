import yagmail
import os
import csv

sender = "whelan.eoin69@gmail.com"
contents = """
I sent this email through Python.\nLet me know if you get it.
"""

if __name__ == "__main__":
    with open("email_config.csv","r") as readfile:
        yag = yagmail.SMTP(user=sender, password=os.getenv("PYTHON_EMAIL_PASSWORD"))
        config = csv.reader(readfile)
        next(config) # skip headers
        for name,address,_ in config:
            #print(f"name is {name}, address is {address}")
            subject = "Hello " + name
            yag.send(to=address, subject=subject, contents=contents)
            print(f"EMAIL sent to {name} at address {address}")