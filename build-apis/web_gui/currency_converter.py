from PyQt6.QtWidgets import QApplication,QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from bs4 import BeautifulSoup
import requests

# If wanted to load from local lib
#import sys, os
#sys.path.append(os.path.abspath(os.path.join("..","access_websites")))
#from currency_rate import get_currency_rate


def get_currency_rate(in_ccy, out_ccy):
    url = f"https://www.x-rates.com/calculator/?from={in_ccy.upper()}&to={out_ccy.upper()}&amount=1"
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")
    out = soup.find("span", class_="ccOutputRslt").get_text()
    return float(out[:-4])

def show_currency():
    input_text = float(text.text())
    # get current selection of dropdown list
    in_ccy = in_combo.currentText()
    out_ccy = target_combo.currentText()
    rate = get_currency_rate(in_ccy, out_ccy)
    output = round(input_text * rate, 2)
    message = f"{input_text} is {output} {out_ccy}"
    output_label.setText(message)



app = QApplication([])
window = QWidget()

window.setWindowTitle("Currency Converter")
layout = QVBoxLayout()


in_combo = QComboBox()
currencies = ["USD", "EUR", "INR", "AUD", "CAD", "GBP"]
in_combo.addItems(currencies)
layout.addWidget(in_combo)


target_combo = QComboBox()
target_combo.addItems(currencies)
layout.addWidget(target_combo)



text = QLineEdit()
layout.addWidget(text)

btn = QPushButton("Convert")
layout.addWidget(btn)

btn.clicked.connect(show_currency)

output_label = QLabel("")
layout.addWidget(output_label)


window.setLayout(layout)
if __name__ == "__main__":
    window.show()
    app.exec()
