import yagmail
import csv
import os

sender = "whelan.eoin69@gmail.com"
#contents = ["Your bill is attached"] # move this within the loop so we can add attachment at sending time

def generate_file(name,amount):
    content = "Your bill is " + amount
    filename = f"bills/{name}-bill.txt" # might be an idea to de-couple adding the extension & writing
    with open(filename, "w") as writefile:
        writefile.write(content)
    return filename


if __name__ == "__main__":
    with open("email_config.csv", "r") as readfile:
        yag = yagmail.SMTP(user=sender, password=os.getenv("PYTHON_EMAIL_PASSWORD"))
        config = csv.reader(readfile)
        next(config) # skip headers
        for name, address, amount in config:
            subject = name + "'s Bill"
            attachment = generate_file(name, amount)
            #contents.append(attachment) # we get caught repeatedly appending if we do this
            contents = ["Your bill is attached", attachment]
            yag.send(to=address, subject=subject, contents=contents)
            print(f"EMAIL sent to {name} at address {address}")