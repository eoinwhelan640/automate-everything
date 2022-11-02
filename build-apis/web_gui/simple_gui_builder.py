from PyQt6.QtWidgets import QApplication,QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit

# Function will operate as a procedure, it shouldnt return anything just modify the widget
def make_sentence():
    # ie text from QLineEdit, the user input option
    input_text = text.text()
    output_label.setText(input_text.capitalize())




# PyQT is made of widgets, signals and slots

app = QApplication([])
window = QWidget()

window.setWindowTitle("Sentence Maker")

# QV is verytical, QH would be horizontal box
layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton("Make")
layout.addWidget(btn)

# button widget, clicked signal, connect method and make_sentence slot
# When button is clicked (signal sent), the slot is invoked. slot should be a function we design
btn.clicked.connect(make_sentence)


output_label = QLabel("")
layout.addWidget(output_label)


# Need to connect the layout object to our window, before doing it, it's just loose
window.setLayout(layout)
# Call this to actually show things
window.show()
# Make the app be in run state
app.exec()


