# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pipinstaller.ui'
#
# Created: Fri Mar 07 17:07:13 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Pipinstaller(object):
    def setupUi(self, Pipinstaller):
        Pipinstaller.setObjectName(_fromUtf8("Pipinstaller"))
        Pipinstaller.resize(400, 380)
        self.gridLayout = QtGui.QGridLayout(Pipinstaller)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Pipinstaller)
        self.label.setMinimumSize(QtCore.QSize(100, 100))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.lineEdit_package_name = QtGui.QLineEdit(Pipinstaller)
        self.lineEdit_package_name.setObjectName(_fromUtf8("lineEdit_package_name"))
        self.gridLayout.addWidget(self.lineEdit_package_name, 1, 0, 1, 2)
        self.pushButton_try_to_install = QtGui.QPushButton(Pipinstaller)
        self.pushButton_try_to_install.setObjectName(_fromUtf8("pushButton_try_to_install"))
        self.gridLayout.addWidget(self.pushButton_try_to_install, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(298, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.textEdit_output = QtGui.QTextEdit(Pipinstaller)
        self.textEdit_output.setMinimumSize(QtCore.QSize(0, 100))
        self.textEdit_output.setObjectName(_fromUtf8("textEdit_output"))
        self.gridLayout.addWidget(self.textEdit_output, 3, 0, 1, 2)

        self.retranslateUi(Pipinstaller)
        QtCore.QMetaObject.connectSlotsByName(Pipinstaller)

    def retranslateUi(self, Pipinstaller):
        Pipinstaller.setWindowTitle(QtGui.QApplication.translate("Pipinstaller", "Pipinstaller", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Pipinstaller", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">To install packages through pip</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Run &quot;pip install package_name&quot; you would install, eg.: pip install qrcode</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">To list packeges installed through pip</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Run &quot;pip list&quot;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_try_to_install.setText(QtGui.QApplication.translate("Pipinstaller", "Exec comand", None, QtGui.QApplication.UnicodeUTF8))

