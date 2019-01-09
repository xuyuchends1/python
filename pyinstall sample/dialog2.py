# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\workspace\python\QT\dialog2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(397, 421)
        self.closeWinBtn = QtWidgets.QPushButton(Dialog2)
        self.closeWinBtn.setGeometry(QtCore.QRect(140, 150, 75, 23))
        self.closeWinBtn.setObjectName("closeWinBtn")

        self.retranslateUi(Dialog2)
        self.closeWinBtn.clicked.connect(Dialog2.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        _translate = QtCore.QCoreApplication.translate
        Dialog2.setWindowTitle(_translate("Dialog2", "Dialog"))
        self.closeWinBtn.setText(_translate("Dialog2", "关闭"))

def main():
    """
    主函数，用于运行程序
    :return: None
    """
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()