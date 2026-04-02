from PyQt6 import QtCore, QtGui, QtWidgets
from urllib.parse import urlparse
import re

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

        ## Ответ
        self.total_answer = QtWidgets.QLabel(parent = self.centralwidget)
        self.total_answer.setGeometry(QtCore.QRect(70, 150, 300, 70))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.total_answer.setFont(font)

        ## Протокол
        self.dan_con = QtWidgets.QLabel(self.centralwidget)
        self.dan_con.setGeometry(QtCore.QRect(50, 190, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dan_con.setFont(font)

        ## кнопка проверки
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 90, 181, 61))
        self.pushButton.setAutoDefault(True)
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

        total_text += f"- протокол: {parsed.scheme}"



        ## Проверка протокола соеденения
        if parsed.scheme == "http":
            self.dan_con.setText("Осторожно соеденение не защищено")
            self.dan_con.setStyleSheet("color: rgb(255, 0, 0);")

            self.dan_con.show()

        else:
            self.dan_con.hide()

        ## Проверка доменного имени
        domen = parsed.netloc
        split_domen = domen.split(".")
        if all(x.isdigit() for x in split_domen):
            total_score += 50


        ## Итоговая оценка
        if total_score > 100:
            self.total_answer.setText("!!!Осторожно высокий риск")
            self.total_answer.setStyleSheet("color: rgb(255, 0, 0);")
        elif total_score > 30 or parsed.scheme != "https":
            self.total_answer.setText("             !Средний риск")
            self.total_answer.setStyleSheet("color: rgb(255, 85, 0);")
        elif parsed.scheme == "https":
            self.total_answer.setText("               Низкий риск")
            self.total_answer.setStyleSheet("color: rgb(0, 255, 0);")
        self.total_answer.show()



        ## Окно вывода
        # self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        # self.textEdit.setGeometry(QtCore.QRect(80, 250, 291, 311))
        # self.textEdit.setTabChangesFocus(True)
        # self.textEdit.setObjectName("textEdit")
        #
        # # Вывод
        # self.textEdit.setText("Hello World")
        #
        # self.textEdit.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
