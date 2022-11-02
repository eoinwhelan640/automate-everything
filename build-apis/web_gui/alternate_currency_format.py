from PyQt6.QtWidgets import QApplication,QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from PyQt6.QtCore import Qt
from bs4 import BeautifulSoup
import requests


def get_currency_rate(in_ccy, out_ccy):
    url = f"https://www.x-rates.com/calculator/?from={in_ccy.upper()}&to={out_ccy.upper()}&amount=1"
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")
    out = soup.find("span", class_="ccOutputRslt").get_text()
    return float(out[:-4])

def show_currency():
    input_text = float(text.text())
    in_ccy = in_combo.currentText()
    out_ccy = target_combo.currentText()
    rate = get_currency_rate(in_ccy, out_ccy)
    output = round(input_text * rate, 2)
    message = f"{input_text} is {output} {out_ccy}"
    output_label.setText(message)



app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency Converter")

# layout variable is the master level and all others are sub layouts within it, ie layout is first in hierarchy
layout = QVBoxLayout()
layout_a = QHBoxLayout()
layout.addLayout(layout_a)


# Adding a sub layout within a sub layout
layout_b = QVBoxLayout()
layout_a.addLayout(layout_b)

layout_c = QVBoxLayout()
layout_a.addLayout(layout_c)


in_combo = QComboBox()
currencies = ["USD", "EUR", "INR", "AUD", "CAD", "GBP"]
in_combo.addItems(currencies)
layout_b.addWidget(in_combo)


target_combo = QComboBox()
target_combo.addItems(currencies)
layout_b.addWidget(target_combo)



text = QLineEdit()
layout_c.addWidget(text)

btn = QPushButton("Convert")
# Align the bottom to the bottom of the layout
layout_c.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)

btn.clicked.connect(show_currency)

output_label = QLabel("")
layout.addWidget(output_label)


window.setLayout(layout)
if __name__ == "__main__":
    window.show()
    app.exec()
