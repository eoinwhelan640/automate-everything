from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtWidgets import QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path


# This class is a bit dodgy, he uses a global variable and two functions for filename, I didnt like that so did this
class FileManager:
    def __init__(self):
        self.filenames = []

    def open_files(self):
        filenames, _ = QFileDialog.getOpenFileNames(window, "Select files")
        self.filenames = filenames
        message.setText('\n'.join(filenames))


    def destroy_files(self):
        for filename in self.filenames:
            path = Path(filename)
            with open(path, "wb") as writefile:
                writefile.write(b"")
            # Deletes the path, ie the object.
            path.unlink()
            self.filenames = []
        message.setText("Destruction successful")



fm = FileManager()

app = QApplication([])
window = QWidget()
window.setWindowTitle("File Destroyer")
layout = QVBoxLayout()

# Notice we can embed html here and PyQt will interpret it
description = QLabel('Select the files you want to destroy.\nThe files will be <font color="red">permanently</font> deleted')
layout.addWidget(description)

open_btn = QPushButton("Open Files")
# ToolTip is the little info box that pops up when you hover the mouse
open_btn.setToolTip("Open File")
#open_btn.setFixedWidth(60) # alter the size of the button
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter) # align to the center
# do something when the button is clicked and connect it to a function - here it's a dialogue box that
# lets the user select files from the filesystem
open_btn.clicked.connect(fm.open_files)

# for a nice interface, what should happen is that we select files for deletion with one button
# Then a button should follow which confirms the deletion
destroy_btn = QPushButton("Destroy files")
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(fm.destroy_files)

message = QLabel("")
layout.addWidget(message)

window.setLayout(layout)
if __name__ == "__main__":
    window.show()
    app.exec()
