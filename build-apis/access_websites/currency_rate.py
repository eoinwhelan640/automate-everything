from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

# create an app instance using flask class
# Good practice to give it the script name
app = Flask(__name__)

# taken from bs currency scraper
def get_currency_rate(in_ccy, out_ccy):
    url = f"https://www.x-rates.com/calculator/?from={in_ccy.upper()}&to={out_ccy.upper()}&amount=1"
    r = requests.get(url).text

    soup = BeautifulSoup(r, "html.parser")
    out = soup.find("span", class_="ccOutputRslt").get_text()
    return float(out[:-4])


# API will consist of two endpoints
# One is the homepage where we will write documentation of API
# / is homepage, this is the first endpoint
@app.route('/')
def home():
    # return some string, making it html formats the page for us
    return "<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>"

# Using <> makes these dynamic inputs later.
# whatever the decorator is attached to MUST have these args or it will not work, it is going to parse them at some
# stage. lets us create dynamically loaded args & input
@app.route("/api/v1/<in_ccy>-<out_ccy>")
def api(in_ccy, out_ccy):
    rate = get_currency_rate(in_ccy, out_ccy)
    result = {'input_ccy': in_ccy, 'output_ccy': out_ccy, 'rate': rate}
    # flask wants json so convert it over
    return jsonify(result)


if __name__=="__main__":
    app.run()