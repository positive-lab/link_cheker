from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit
import sys

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    main_text = QtWidgets.QLabel(window)
    main_text.setText("Hello World")
    main_text.move(100, 100)

    window.setWindowTitle("Простая программа")
    window.setGeometry(300, 250, 350, 200)

    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    application()