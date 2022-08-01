# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_DialogWindow(object):
    def setupUi(self, DialogWindow):
        if not DialogWindow.objectName():
            DialogWindow.setObjectName(u"DialogWindow")
        DialogWindow.resize(309, 155)
        self.horizontalLayout = QHBoxLayout(DialogWindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(DialogWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.nameBox = QLabel(self.groupBox)
        self.nameBox.setObjectName(u"nameBox")

        self.verticalLayout_2.addWidget(self.nameBox)

        self.nameLine = QLineEdit(self.groupBox)
        self.nameLine.setObjectName(u"nameLine")

        self.verticalLayout_2.addWidget(self.nameLine)

        self.passwdLine = QLineEdit(self.groupBox)
        self.passwdLine.setObjectName(u"passwdLine")
        self.passwdLine.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.passwdLine)

        self.dialogBox = QDialogButtonBox(self.groupBox)
        self.dialogBox.setObjectName(u"dialogBox")
        self.dialogBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.dialogBox.setCenterButtons(False)

        self.verticalLayout_2.addWidget(self.dialogBox)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addWidget(self.groupBox)


        self.retranslateUi(DialogWindow)

        QMetaObject.connectSlotsByName(DialogWindow)
    # setupUi

    def retranslateUi(self, DialogWindow):
        DialogWindow.setWindowTitle("")
        self.groupBox.setTitle(QCoreApplication.translate("DialogWindow", u"Login Daten", None))
        self.nameBox.setText("")
        self.nameLine.setPlaceholderText(QCoreApplication.translate("DialogWindow", u"Nutzername", None))
        self.passwdLine.setPlaceholderText(QCoreApplication.translate("DialogWindow", u"Passwort", None))
    # retranslateUi

