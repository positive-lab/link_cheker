from PyQt6 import QtCore, QtGui, QtWidgets
from urllib.parse import urlparse


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(450, 600)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")

        ## Центральные виджеты хз для чего это
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ## Поле для ввода
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 10, 450, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")

        ## кнопка проверки
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 90, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.answer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Проверка ссылок"))
        self.pushButton.setText(_translate("MainWindow", "Проверить"))

    def answer(self):
        total_score = 0
        total_text = ""
        url = self.lineEdit.text()
        parsed = urlparse(url)

        ## Проверка протокола
        if not parsed.scheme == "https":
            total_score += 40
        total_text += f"- протокол: {parsed.scheme}"

        ## Проверяем есть ли домен или просто ip
        if parsed.netloc.isdigit():
            total_score += 50
            total_text += "\n- используется ip вместо домена"

        ## Итоговая оценка
        self.total = QtWidgets.QLabel(parent = self.centralwidget)
        # self.total.move(70, 160)
        # self.total.adjustSize()
        self.total.setGeometry(QtCore.QRect(70, 160, 300, 70))

        if total_score > 30:
            self.total.setText("!Средний риск \nстоит проверить тщательнее")
            self.total.setStyleSheet("color: rgb(255, 85, 0);")
        elif total_score > 100:
            self.total.setText("!!!Осторожно высокий риск \nлучше вообще не не трогать")
            self.total.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.total.setText("Низкий риск можно переходить")
            self.total.setStyleSheet("color: rgb(0, 255, 0);")

        self.total.show()


        ## Окно вывода
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 250, 291, 311))
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.setObjectName("textEdit")

        ## Вывод
        self.textEdit.setText(total_text)

        self.textEdit.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
