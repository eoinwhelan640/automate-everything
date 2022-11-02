from flask import Flask

# This app relies on using REPL, your mans website. Would have to make own server/backend or use cloud if wanted to
# deploy another way

app = Flask(__name__)

# when visitor accesses the website, we have a decorator for each url in the website
# This one is homepage - returning string here but in real website you'd want html for a nice website
@app.route("/")
def home():
    return "Welcome to my website"

# When deployed on repl, it listen for stuff on localhost and creates a url for it. For us, it will work on localhost
# but needs more to be deployed as it's own thing.
app.run('0.0.0.0')