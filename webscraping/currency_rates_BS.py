from bs4 import BeautifulSoup
import requests


def get_currency(in_ccy:str, out_ccy: str)-> float:
    url = f"https://www.x-rates.com/calculator/?from={in_ccy.upper()}&to={out_ccy.upper()}&amount=1"
    content = requests.get(url).text
    # Tell BeautifulSoup to use a html parser. Could be other format like xl or something we'd need to parse
    # The soup itself is kind of still the page source, but is almost like a mapping or integrated structure/scaffold
    # we can browse easier.
    soup = BeautifulSoup(content, "html.parser")
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    return float(rate[:-4])


if __name__ == "__main__":
    print(get_currency("EUR", "USD"))