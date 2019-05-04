from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
import re, password, pyperclip

global num_of_digits, passwd, a
num_of_digits = 8
passwd = 'qwerty123'
a = 4

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "Password Generator V1.0"
        self.top = 200
        self.left = 400
        self.width = 400
        self.height = 200
        self.iconName = "icon.png"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createLayout()

        global vbox

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        self.checkbox_copyBtn()

        self.label = QLabel()
        vbox.addWidget(self.label)
        self.setLayout(vbox)

        self.show()

    def createLayout(self):
        self.groupBox = QGroupBox("Passwords as strong as hercules")
        self.groupBox.setFont(QtGui.QFont("Sanserif ", 10))

        global hboxlayout

        hboxlayout = QHBoxLayout()

        self.radiobtn1 = QRadioButton("8 characters")
        self.radiobtn1.setChecked(True)
        self.radiobtn1.toggled.connect(self.OnRadioBtn)
        hboxlayout.addWidget(self.radiobtn1)

        self.radiobtn2 = QRadioButton("12 characters")
        self.radiobtn2.toggled.connect(self.OnRadioBtn)
        hboxlayout.addWidget(self.radiobtn2)

        self.radiobtn3 = QRadioButton("16 characters")
        self.radiobtn3.toggled.connect(self.OnRadioBtn)
        hboxlayout.addWidget(self.radiobtn3)

        self.radiobtn4 = QRadioButton("20 characters")
        self.radiobtn4.toggled.connect(self.OnRadioBtn)
        hboxlayout.addWidget(self.radiobtn4)

        button = QPushButton("Get Password", self)
        button.setGeometry(QRect(250, 50, 111, 28))
        button.setToolTip("<h6>Click to get password</h6>")
        button.clicked.connect(self.OnClicked)

        hboxlayout.addWidget(button)

        self.groupBox.setLayout(hboxlayout)

    def checkbox_copyBtn(self):
        self.check1 = QCheckBox("Add Numbers")
        self.check1.toggled.connect(self.onCheckBox_Toggled)
        vbox.addWidget(self.check1)

        self.check2 = QCheckBox("Add Special Characters")
        self.check2.toggled.connect(self.onCheckBox_Toggled)
        vbox.addWidget(self.check2)

        button1 = QPushButton("Copy", self)
        button1.setGeometry(QRect(480, 158, 121, 19))
        button1.setToolTip("<h6>Copy password to clipboard</h6>")
        button1.clicked.connect(self.OnClickedCopy)
        vbox.addWidget(button1)

    def onCheckBox_Toggled(self):
        global a
        if self.check1.isChecked() and self.check2.isChecked():
            a = 3
        elif self.check1.isChecked():
            a = 1
        elif self.check2.isChecked():
            a = 2

    def OnRadioBtn(self):
        radioBtn = self.sender()
        global num_of_digits

        if radioBtn.isChecked():
            self.label.setText("You have selected " + radioBtn.text() + ", Bitch!")
            num_of_digits = re.search(r"\d+", radioBtn.text())
            num_of_digits = int(num_of_digits.group(0))

    def OnClicked(self):
        global num_of_digits, passwd
        passwd = password.generatePassword(num_of_digits,a)
        self.label.setText(passwd)

    def OnClickedCopy(self):
        global passwd
        pyperclip.copy(passwd)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
