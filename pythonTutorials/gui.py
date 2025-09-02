# I will use PySide6 for the gui
# It uses the Qt framework

from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow
from PySide6.QtCore import Qt

class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("test window title")

        label = QLabel("test label")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("""
                            background-color: #F527D3;
                            color: #28FF1C;
                            """)

        self.setCentralWidget(label)

app = QApplication()

window = Main()

button = QPushButton()
button.setText("test button")

window.show()
button.show()

app.exec()
