# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def add(self):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.plainTextEdit_3.setPlainText(_translate("Form", str(int(self.plainTextEdit.toPlainText())+int(self.plainTextEdit_2.toPlainText()))))
    def sub(self):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.plainTextEdit_3.setPlainText(_translate("Form", str(int(self.plainTextEdit.toPlainText())-int(self.plainTextEdit_2.toPlainText()))))
    def mul(self):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.plainTextEdit_3.setPlainText(_translate("Form", str(int(self.plainTextEdit.toPlainText())/int(self.plainTextEdit_2.toPlainText()))))
    def div(self):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.plainTextEdit_3.setPlainText(_translate("Form", str(int(self.plainTextEdit.toPlainText())*int(self.plainTextEdit_2.toPlainText()))))

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 230, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 230, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 190, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 47, 13))
        self.label_3.setObjectName("label_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(120, 20, 181, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(120, 70, 181, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(120, 120, 181, 31))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.sub)
        self.pushButton_3.clicked.connect(self.mul)
        self.pushButton_4.clicked.connect(self.div)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "ADD"))
        self.pushButton_2.setText(_translate("Form", "SUB"))
        self.pushButton_3.setText(_translate("Form", "DIV"))
        self.pushButton_4.setText(_translate("Form", "MUL"))
        self.label.setText(_translate("Form", "Operand 1"))
        self.label_2.setText(_translate("Form", "Operand 2"))
        self.label_3.setText(_translate("Form", "Result"))
        self.plainTextEdit.setPlainText(_translate("Form", "0"))
        self.plainTextEdit_2.setPlainText(_translate("Form", "0"))
        self.plainTextEdit_3.setPlainText(_translate("Form", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

