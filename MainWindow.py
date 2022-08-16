# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTextBrowser,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(442, 749)
        self.action_Zugangsdaten = QAction(MainWindow)
        self.action_Zugangsdaten.setObjectName(u"action_Zugangsdaten")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Tabs = QTabWidget(self.centralwidget)
        self.Tabs.setObjectName(u"Tabs")
        self.Page1 = QWidget()
        self.Page1.setObjectName(u"Page1")
        self.gridLayout = QGridLayout(self.Page1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.getList = QPushButton(self.Page1)
        self.getList.setObjectName(u"getList")

        self.horizontalLayout_4.addWidget(self.getList)

        self.readList = QPushButton(self.Page1)
        self.readList.setObjectName(u"readList")

        self.horizontalLayout_4.addWidget(self.readList)


        self.gridLayout.addLayout(self.horizontalLayout_4, 30, 1, 1, 3)

        self.automatic_continue = QCheckBox(self.Page1)
        self.automatic_continue.setObjectName(u"automatic_continue")
        self.automatic_continue.setMaximumSize(QSize(70, 16777215))
        self.automatic_continue.setChecked(False)

        self.gridLayout.addWidget(self.automatic_continue, 35, 2, 1, 1)

        self.error_field = QLabel(self.Page1)
        self.error_field.setObjectName(u"error_field")

        self.gridLayout.addWidget(self.error_field, 34, 1, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.Page1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.backward = QPushButton(self.Page1)
        self.backward.setObjectName(u"backward")
        self.backward.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_3.addWidget(self.backward)

        self.row_field = QLineEdit(self.Page1)
        self.row_field.setObjectName(u"row_field")
        self.row_field.setMaximumSize(QSize(50, 16777215))
        self.row_field.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.row_field)

        self.forward = QPushButton(self.Page1)
        self.forward.setObjectName(u"forward")
        self.forward.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_3.addWidget(self.forward)

        self.label = QLabel(self.Page1)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(10, 16777215))

        self.horizontalLayout_3.addWidget(self.label)

        self.list_field = QLabel(self.Page1)
        self.list_field.setObjectName(u"list_field")
        self.list_field.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.list_field)


        self.gridLayout.addLayout(self.horizontalLayout_3, 29, 1, 1, 3)

        self.buttonNew = QPushButton(self.Page1)
        self.buttonNew.setObjectName(u"buttonNew")
        self.buttonNew.setMaximumSize(QSize(150, 16777215))
        self.buttonNew.setAutoDefault(False)

        self.gridLayout.addWidget(self.buttonNew, 35, 3, 1, 1)

        self.groupBox_2 = QGroupBox(self.Page1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFlat(True)
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lname = QLineEdit(self.groupBox_2)
        self.lname.setObjectName(u"lname")
        self.lname.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.lname, 0, 1, 1, 1)

        self.telephone = QLineEdit(self.groupBox_2)
        self.telephone.setObjectName(u"telephone")
        self.telephone.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.telephone, 2, 1, 1, 1)

        self.uid = QLineEdit(self.groupBox_2)
        self.uid.setObjectName(u"uid")
        self.uid.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.uid, 5, 0, 1, 1)

        self.fname = QLineEdit(self.groupBox_2)
        self.fname.setObjectName(u"fname")
        self.fname.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.fname, 0, 0, 1, 1)

        self.mail = QLineEdit(self.groupBox_2)
        self.mail.setObjectName(u"mail")
        self.mail.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.mail, 2, 0, 1, 1)

        self.role = QLineEdit(self.groupBox_2)
        self.role.setObjectName(u"role")
        self.role.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.role, 3, 1, 1, 1)

        self.facility = QLineEdit(self.groupBox_2)
        self.facility.setObjectName(u"facility")
        self.facility.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.facility, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 3)

        self.groupBox = QGroupBox(self.Page1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(True)
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.it_support = QCheckBox(self.groupBox)
        self.it_support.setObjectName(u"it_support")

        self.gridLayout_3.addWidget(self.it_support, 2, 0, 1, 1)

        self.diversity = QCheckBox(self.groupBox)
        self.diversity.setObjectName(u"diversity")

        self.gridLayout_3.addWidget(self.diversity, 4, 0, 1, 1)

        self.dig_marketing = QCheckBox(self.groupBox)
        self.dig_marketing.setObjectName(u"dig_marketing")

        self.gridLayout_3.addWidget(self.dig_marketing, 0, 1, 1, 1)

        self.vertrieb_verkauf = QCheckBox(self.groupBox)
        self.vertrieb_verkauf.setObjectName(u"vertrieb_verkauf")

        self.gridLayout_3.addWidget(self.vertrieb_verkauf, 1, 1, 1, 1)

        self.grafikdesign = QCheckBox(self.groupBox)
        self.grafikdesign.setObjectName(u"grafikdesign")

        self.gridLayout_3.addWidget(self.grafikdesign, 3, 0, 1, 1)

        self.kundenservice = QCheckBox(self.groupBox)
        self.kundenservice.setObjectName(u"kundenservice")

        self.gridLayout_3.addWidget(self.kundenservice, 1, 0, 1, 1)

        self.finanzanalyse = QCheckBox(self.groupBox)
        self.finanzanalyse.setObjectName(u"finanzanalyse")

        self.gridLayout_3.addWidget(self.finanzanalyse, 5, 0, 1, 1)

        self.dynamics = QCheckBox(self.groupBox)
        self.dynamics.setObjectName(u"dynamics")

        self.gridLayout_3.addWidget(self.dynamics, 9, 0, 1, 1)

        self.soft_skills = QCheckBox(self.groupBox)
        self.soft_skills.setObjectName(u"soft_skills")

        self.gridLayout_3.addWidget(self.soft_skills, 2, 1, 1, 1)

        self.dig_arbeitsplatz = QCheckBox(self.groupBox)
        self.dig_arbeitsplatz.setObjectName(u"dig_arbeitsplatz")

        self.gridLayout_3.addWidget(self.dig_arbeitsplatz, 6, 0, 1, 1)

        self.it_administration = QCheckBox(self.groupBox)
        self.it_administration.setObjectName(u"it_administration")

        self.gridLayout_3.addWidget(self.it_administration, 7, 0, 1, 1)

        self.projektmanagement = QCheckBox(self.groupBox)
        self.projektmanagement.setObjectName(u"projektmanagement")

        self.gridLayout_3.addWidget(self.projektmanagement, 8, 0, 1, 1)

        self.empfang = QCheckBox(self.groupBox)
        self.empfang.setObjectName(u"empfang")
        self.empfang.setChecked(True)

        self.gridLayout_3.addWidget(self.empfang, 0, 0, 1, 1)

        self.jobcoaching = QCheckBox(self.groupBox)
        self.jobcoaching.setObjectName(u"jobcoaching")

        self.gridLayout_3.addWidget(self.jobcoaching, 3, 1, 1, 1)

        self.power_platform = QCheckBox(self.groupBox)
        self.power_platform.setObjectName(u"power_platform")

        self.gridLayout_3.addWidget(self.power_platform, 10, 0, 1, 1)

        self.mc_af = QCheckBox(self.groupBox)
        self.mc_af.setObjectName(u"mc_af")

        self.gridLayout_3.addWidget(self.mc_af, 4, 1, 1, 1)

        self.mc_adf = QCheckBox(self.groupBox)
        self.mc_adf.setObjectName(u"mc_adf")

        self.gridLayout_3.addWidget(self.mc_adf, 5, 1, 1, 1)

        self.mc_aaf = QCheckBox(self.groupBox)
        self.mc_aaf.setObjectName(u"mc_aaf")

        self.gridLayout_3.addWidget(self.mc_aaf, 6, 1, 1, 1)

        self.softwareentwicklung = QCheckBox(self.groupBox)
        self.softwareentwicklung.setObjectName(u"softwareentwicklung")

        self.gridLayout_3.addWidget(self.softwareentwicklung, 7, 1, 1, 1)

        self.datenanalyse = QCheckBox(self.groupBox)
        self.datenanalyse.setObjectName(u"datenanalyse")

        self.gridLayout_3.addWidget(self.datenanalyse, 8, 1, 1, 1)

        self.microsoft = QCheckBox(self.groupBox)
        self.microsoft.setObjectName(u"microsoft")

        self.gridLayout_3.addWidget(self.microsoft, 9, 1, 1, 1)

        self.teams = QCheckBox(self.groupBox)
        self.teams.setObjectName(u"teams")

        self.gridLayout_3.addWidget(self.teams, 10, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 16, 1, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 37, 1, 1, 3)

        self.progress = QProgressBar(self.Page1)
        self.progress.setObjectName(u"progress")
        self.progress.setValue(0)

        self.gridLayout.addWidget(self.progress, 33, 1, 1, 3)

        self.Tabs.addTab(self.Page1, "")
        self.Page2 = QWidget()
        self.Page2.setObjectName(u"Page2")
        self.gridLayoutWidget = QWidget(self.Page2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 401, 641))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.status_field = QTextBrowser(self.gridLayoutWidget)
        self.status_field.setObjectName(u"status_field")

        self.gridLayout_2.addWidget(self.status_field, 8, 0, 1, 1)

        self.tempPasswd = QCheckBox(self.gridLayoutWidget)
        self.tempPasswd.setObjectName(u"tempPasswd")

        self.gridLayout_2.addWidget(self.tempPasswd, 3, 0, 1, 1)

        self.changePasswd = QPushButton(self.gridLayoutWidget)
        self.changePasswd.setObjectName(u"changePasswd")

        self.gridLayout_2.addWidget(self.changePasswd, 4, 0, 1, 1)

        self.selfChosenPasswd = QLineEdit(self.gridLayoutWidget)
        self.selfChosenPasswd.setObjectName(u"selfChosenPasswd")
        self.selfChosenPasswd.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.selfChosenPasswd, 2, 0, 1, 1)

        self.textfield = QLabel(self.gridLayoutWidget)
        self.textfield.setObjectName(u"textfield")

        self.gridLayout_2.addWidget(self.textfield, 7, 0, 1, 1)

        self.deleteAccount = QPushButton(self.gridLayoutWidget)
        self.deleteAccount.setObjectName(u"deleteAccount")

        self.gridLayout_2.addWidget(self.deleteAccount, 5, 0, 1, 1)

        self.search = QPushButton(self.gridLayoutWidget)
        self.search.setObjectName(u"search")

        self.gridLayout_2.addWidget(self.search, 1, 0, 1, 1)

        self.searchField = QLineEdit(self.gridLayoutWidget)
        self.searchField.setObjectName(u"searchField")
        self.searchField.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.searchField, 0, 0, 1, 1)

        self.Tabs.addTab(self.Page2, "")

        self.horizontalLayout.addWidget(self.Tabs)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 442, 43))
        self.menu_Einstellungen = QMenu(self.menubar)
        self.menu_Einstellungen.setObjectName(u"menu_Einstellungen")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_Einstellungen.menuAction())
        self.menu_Einstellungen.addAction(self.action_Zugangsdaten)

        self.retranslateUi(MainWindow)

        self.Tabs.setCurrentIndex(0)
        self.buttonNew.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Account Manager", None))
        self.action_Zugangsdaten.setText(QCoreApplication.translate("MainWindow", u"&Zugangsdaten", None))
        self.getList.setText(QCoreApplication.translate("MainWindow", u"Aktuelle Liste laden", None))
        self.readList.setText(QCoreApplication.translate("MainWindow", u"Account einlesen", None))
        self.automatic_continue.setText(QCoreApplication.translate("MainWindow", u"weiter", None))
        self.error_field.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Zeile", None))
        self.backward.setText(QCoreApplication.translate("MainWindow", u"\u2b05", None))
        self.row_field.setText("")
        self.row_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-", None))
        self.forward.setText(QCoreApplication.translate("MainWindow", u"\u27a1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.list_field.setText(QCoreApplication.translate("MainWindow", u"\u221e", None))
        self.buttonNew.setText(QCoreApplication.translate("MainWindow", u"Account erstellen", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Stammdaten", None))
        self.lname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nachname", None))
        self.telephone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefon", None))
        self.uid.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID (Standard: it, - f\u00fcr leer)", None))
        self.fname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Vorname", None))
        self.mail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-Mail", None))
        self.role.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rolle", None))
        self.facility.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Einrichtung", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Gruppen", None))
        self.it_support.setText(QCoreApplication.translate("MainWindow", u"IT-Support", None))
        self.diversity.setText(QCoreApplication.translate("MainWindow", u"Diversity", None))
        self.dig_marketing.setText(QCoreApplication.translate("MainWindow", u"Digitales Marketing", None))
        self.vertrieb_verkauf.setText(QCoreApplication.translate("MainWindow", u"Vertrieb und Verkauf", None))
        self.grafikdesign.setText(QCoreApplication.translate("MainWindow", u"Grafikdesign", None))
        self.kundenservice.setText(QCoreApplication.translate("MainWindow", u"Kundenservice", None))
        self.finanzanalyse.setText(QCoreApplication.translate("MainWindow", u"Finanzanalyse", None))
        self.dynamics.setText(QCoreApplication.translate("MainWindow", u"Dynamics 365", None))
        self.soft_skills.setText(QCoreApplication.translate("MainWindow", u"Soft Skills", None))
        self.dig_arbeitsplatz.setText(QCoreApplication.translate("MainWindow", u"Digitaler Arbeitsplatz", None))
        self.it_administration.setText(QCoreApplication.translate("MainWindow", u"IT-Administration", None))
        self.projektmanagement.setText(QCoreApplication.translate("MainWindow", u"Projektmanagement", None))
        self.empfang.setText(QCoreApplication.translate("MainWindow", u"Empfang", None))
        self.jobcoaching.setText(QCoreApplication.translate("MainWindow", u"Jobcoaching", None))
        self.power_platform.setText(QCoreApplication.translate("MainWindow", u"Power Platform", None))
        self.mc_af.setText(QCoreApplication.translate("MainWindow", u"Azure", None))
        self.mc_adf.setText(QCoreApplication.translate("MainWindow", u"Azure Data", None))
        self.mc_aaf.setText(QCoreApplication.translate("MainWindow", u"Azure AI", None))
        self.softwareentwicklung.setText(QCoreApplication.translate("MainWindow", u"Softwareentwicklung", None))
        self.datenanalyse.setText(QCoreApplication.translate("MainWindow", u"Datenanalyse", None))
        self.microsoft.setText(QCoreApplication.translate("MainWindow", u"Microsoft 365", None))
        self.teams.setText(QCoreApplication.translate("MainWindow", u"Microsoft Teams", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Page1), QCoreApplication.translate("MainWindow", u"Aus Tabelle erstellen", None))
        self.tempPasswd.setText(QCoreApplication.translate("MainWindow", u"tempor\u00e4res Passwort", None))
        self.changePasswd.setText(QCoreApplication.translate("MainWindow", u"Passwort \u00e4ndern", None))
        self.selfChosenPasswd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Passwort eingeben,  leer f\u00fcr automatisch erstellen", None))
        self.textfield.setText(QCoreApplication.translate("MainWindow", u"Ausgabe:", None))
        self.deleteAccount.setText(QCoreApplication.translate("MainWindow", u"Account l\u00f6schen", None))
        self.search.setText(QCoreApplication.translate("MainWindow", u"Account suchen", None))
        self.searchField.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name des Accounts", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Page2), QCoreApplication.translate("MainWindow", u"Account bearbeiten", None))
        self.menu_Einstellungen.setTitle(QCoreApplication.translate("MainWindow", u"&Einstellungen", None))
    # retranslateUi

