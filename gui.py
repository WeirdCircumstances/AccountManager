from PySide6.QtGui import QIcon
from PySide6.QtCore import (
    QThreadPool,
)
from PySide6.QtWidgets import (
    QMainWindow,
)

from MainWindow import Ui_MainWindow
from needpermissions import CheckPermissons

from web import Downloader
from userdata import user, behavior_control
from cloudshell import ADWorker, ADmanage

import string
import random
import pandas as pd
import os


# PySide6
class MainWindow(QMainWindow, Ui_MainWindow):
    automatic_continue_value = False

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # self.show()

        self.dialog = None

        self.threadpool = QThreadPool()

        self.setIcon()

        self.fname.textEdited.connect(self.fname_changed)

        self.lname.textEdited.connect(self.lname_changed)

        self.mail.textEdited.connect(self.mail_changed)

        self.telephone.textEdited.connect(self.telephone_changed)

        self.facility.textEdited.connect(self.facility_changed)

        self.role.textEdited.connect(self.role_changed)

        self.uid.textEdited.connect(self.uid_changed)

        self.empfang.stateChanged.connect(self.empfang_toggle)

        self.kundenservice.stateChanged.connect(self.kundenservice_toggle)

        self.it_support.stateChanged.connect(self.it_support_toggle)

        self.grafikdesign.stateChanged.connect(self.grafikdesign_toggle)

        self.diversity.stateChanged.connect(self.diversity_toggle)

        self.finanzanalyse.stateChanged.connect(self.finanzanalyse_toggle)

        self.dig_arbeitsplatz.stateChanged.connect(self.dig_arbeitsplatz_toggle)

        self.it_administration.stateChanged.connect(self.it_administration_toggle)

        self.projektmanagement.stateChanged.connect(self.projektmanagement_toggle)

        self.dynamics.stateChanged.connect(self.dynamics_toggle)

        self.power_platform.stateChanged.connect(self.power_platform_toggle)

        self.dig_marketing.stateChanged.connect(self.dig_marketing_toggle)

        self.vertrieb_verkauf.stateChanged.connect(self.vertrieb_verkauf_toggle)

        self.soft_skills.stateChanged.connect(self.soft_skills_toggle)

        self.jobcoaching.stateChanged.connect(self.jobcoaching_toggle)

        self.mc_af.stateChanged.connect(self.mc_af_toggle)

        self.mc_adf.stateChanged.connect(self.mc_adf_toggle)

        self.mc_aaf.stateChanged.connect(self.mc_aaf_toggle)

        self.softwareentwicklung.stateChanged.connect(self.softwareentwicklung_toggle)

        self.datenanalyse.stateChanged.connect(self.datenanalyse_toggle)

        self.microsoft.stateChanged.connect(self.microsoft_toggle)

        self.teams.stateChanged.connect(self.teams_toggle)

        self.backward.clicked.connect(self.backward_click)

        self.forward.clicked.connect(self.forward_click)

        self.row_field.textEdited.connect(self.row_changed)

        self.getList.clicked.connect(self.get_new_account_List)

        self.readList.clicked.connect(self.get_account_from_List)

        # self.buttonNew.setObjectName("buttonNew")
        self.buttonNew.setStyleSheet("QPushButton#buttonNew:hover {background-color: red;}")
        self.buttonNew.clicked.connect(self.generate_single_account)

        self.automatic_continue.stateChanged.connect(self.toggle_automatic_continue)

        # Second Tab

        self.searchField.textEdited.connect(self.search_field)

        self.search.clicked.connect(self.search_account)

        self.selfChosenPasswd.textEdited.connect(self.chosen_passwd)

        self.tempPasswd.stateChanged.connect(self.temp_passwd)

        self.changePasswd.clicked.connect(self.change_passwd)
        self.changePasswd.setStyleSheet("QPushButton#changePasswd:hover {background-color: green;}")

        self.deleteAccount.clicked.connect(self.delete_account)
        self.deleteAccount.setStyleSheet("QPushButton#deleteAccount:hover {background-color: red;}")

        # get new Anmeldung Kurs.csv, afterwards read last value or jump to the end of the list, when there is no row_number file
        self.get_new_account_List()

    def fname_changed(self, s):
        user['fname'] = s.lstrip().strip('\n').strip().title()

    def lname_changed(self, s):
        user['lname'] = s.lstrip().strip('\n').strip().title()

    def facility_changed(self, s):
        user['facility'] = s.lstrip().strip('\n').strip()

    def role_changed(self, s):
        user['role'] = s.lstrip().strip('\n').strip()

    def telephone_changed(self, s):
        user['telephone'] = s.lstrip().strip('\n').strip()

    def mail_changed(self, s):
        user['mail'] = s.lstrip().strip('\n').strip()

    def uid_changed(self, s):
        if s == '':
            s = 'it.'
        if s == '-':
            s = ''
        else:
            s = s + '.'

        user['uid'] = s

    def empfang_toggle(self, s):
        user['empfang'] = s

    def kundenservice_toggle(self, s):
        user['kundenservice'] = s

    def it_support_toggle(self, s):
        user['it_support'] = s

    def grafikdesign_toggle(self, s):
        user['grafikdesign'] = s

    def diversity_toggle(self, s):
        user['diversity'] = s

    def finanzanalyse_toggle(self, s):
        user['finanzanalyse'] = s

    def dig_arbeitsplatz_toggle(self, s):
        user['dig_arbeitsplatz'] = s

    def it_administration_toggle(self, s):
        user['it_administration'] = s

    def projektmanagement_toggle(self, s):
        user['projektmanagement'] = s

    def dig_marketing_toggle(self, s):
        user['dig_marketing'] = s

    def mc_adf_toggle(self, s):
        user['mc_adf'] = s

    def vertrieb_verkauf_toggle(self, s):
        user['vertrieb_verkauf'] = s

    def mc_af_toggle(self, s):
        user['mc_af'] = s

    def soft_skills_toggle(self, s):
        user['soft_skills'] = s

    def jobcoaching_toggle(self, s):
        user['jobcoaching'] = s

    def mc_aaf_toggle(self, s):
        user['mc_aaf'] = s

    def softwareentwicklung_toggle(self, s):
        user['softwareentwicklung'] = s

    def datenanalyse_toggle(self, s):
        user['datenanalyse'] = s

    def dynamics_toggle(self, s):
        user['dynamics365'] = s

    def microsoft_toggle(self, s):
        user['microsoft365'] = s

    def power_platform_toggle(self, s):
        user['power_platform'] = s

    def teams_toggle(self, s):
        user['teams'] = s

    def calculate_email(self):
        domain = "@innovative-students.de"

        short_fname = user['fname'][:6].replace(" ", "").replace("-", "").lower()
        short_lname = user['lname'][:6].replace(" ", "").replace("-", "").lower()

        if 'Student' in user['role']:
            short_mail = 'edu.' + short_fname + short_lname
            user['uid'] = 'edu'
        else:
            short_mail = 'it.' + short_fname + short_lname
            user['uid'] = 'it'
            # short_mail = user['uid'] + short_fname + short_lname

        short_mail = short_mail.lower()
        short_mail = short_mail.replace("ä", "ae")
        short_mail = short_mail.replace("á", "ae")
        short_mail = short_mail.replace("é", "e")
        short_mail = short_mail.replace("è", "e")
        short_mail = short_mail.replace("í", "i")
        short_mail = short_mail.replace("ö", "oe")
        short_mail = short_mail.replace("ó", "o")
        short_mail = short_mail.replace("ò", "o")
        short_mail = short_mail.replace("ô", "o")
        short_mail = short_mail.replace("ø", "o")
        short_mail = short_mail.replace("ü", "ue")
        short_mail = short_mail.replace("ú", "u")
        short_mail = short_mail.replace("ß", "ss")
        short_mail = short_mail.replace("ç", "c")

        user['it_mail'] = short_mail

        # full_mail = short_mail + domain

    def generate_passwd(self):
        upper_chars = string.ascii_uppercase
        lower_chars = string.ascii_lowercase
        random_digits = string.digits

        upper = ''.join(random.choice(upper_chars) for _ in range(1))
        lower = ''.join(random.choice(lower_chars) for _ in range(2))
        digits = ''.join(random.choice(random_digits) for _ in range(5))

        passwd = upper + lower + digits

        user['passwd'] = passwd

    def search_field(self, s):
        user['search'] = s

    def search_account(self):
        # self.status_field.setText("Suche nach: " + search)
        # implement search here

        worker = ADmanage(self)

        self.show_status("")
        worker.signals.error.connect(self.show_status)

        self.threadpool.start(worker.search(user['search']))

    def chosen_passwd(self, s):
        user['passwd'] = s

    def temp_passwd(self, s):
        user['tmp_passwd'] = s

    def change_passwd(self):
        self.status_field.setText("")
        if user['passwd'] == '':
            self.generate_passwd()

        worker = ADmanage(self)

        self.show_status("")
        worker.signals.error.connect(self.show_status)

        self.threadpool.start(worker.set_passwd(user['passwd']))

    def delete_account(self):
        # self.status_field.setText("Nicht implementiert.")

        worker = ADmanage(self)

        worker.signals.error.connect(self.show_status)

        self.threadpool.start(worker.delete_account(user['principalName']))

    def show_status(self, error):
        self.status_field.setText(error)

    def setIcon(self):
        app_icon = QIcon("happy-document.png")
        self.setWindowIcon(app_icon)

    def get_new_account_List(self):
        if os.path.exists("Anmeldung Kurs.csv"):
            os.remove("Anmeldung Kurs.csv")
        else:
            print("Anmeldung Kurs.csv does not exists.")

        self.show_error("Lade aktuelle Liste")

        self.login = "it-fitness-Redaktion"

        self.permission = CheckPermissons(self.dialog, self.login)
        self.permission.signals.error.connect(self.show_error)

        if self.permission.check():
            worker = Downloader()
            worker.signals.progress.connect(self.generate_progress)
            self.show_error("")
            worker.signals.error.connect(self.show_error)
            worker.signals.finished.connect(self.get_account_from_List)

            self.threadpool.start(worker)

    def generate_single_account(self):

        if user['fname'] == "" or user['lname'] == "":
            self.show_error("Name darf nicht leer sein")
        else:
            self.calculate_email()
            self.generate_passwd()

            print(user)

            # self.login = "innovative-students.de"

            # self.permission = CheckPermissons(self.dialog, self.login)
            # self.permission.signals.error.connect(self.show_error)

            # self.result = self.permission.check()

            # if self.permission.check():
            # worker = WebWorker()
            worker = ADWorker()
            worker.signals.progress.connect(self.generate_progress)
            self.show_error("")
            worker.signals.error.connect(self.show_error)

            self.threadpool.start(worker)

    def generate_progress(self, progress):
        self.progress.setValue(progress)

        if progress < 100:
            self.buttonNew.setEnabled(False)
            self.readList.setEnabled(False)
            self.getList.setEnabled(False)
        else:
            if self.automatic_continue.isChecked():
                self.get_account_from_List()
                self.generate_single_account()
            else:
                self.buttonNew.setEnabled(True)
                self.readList.setEnabled(True)
                self.getList.setEnabled(True)
                self.get_account_from_List()

    def toggle_automatic_continue(self, s):
        # if progress == 100:
        if s:
            self.buttonNew.setEnabled(True)
            self.readList.setEnabled(True)
            self.getList.setEnabled(True)
        else:
            self.buttonNew.setEnabled(False)
            self.readList.setEnabled(False)
            self.getList.setEnabled(False)

    def show_error(self, error):
        self.error_field.setText(error)

    def get_account_from_List(self):
        # print(s)
        self.show_error("")

        # print(self.read_entries_from_csv)
        self.read_entries_from_csv()

        # self.button_toggle()

    def backward_click(self):
        row = int(self.get_row_number())
        row -= 1
        self.row_field.setText(str(row))
        self.row_changed(str(row))
        self.get_account_from_List()
        self.forward.setEnabled(True)

    def forward_click(self):
        row = int(self.get_row_number())
        row += 1
        self.row_field.setText(str(row))
        self.row_changed(str(row))
        self.get_account_from_List()

    def get_row_number(self):
        if os.path.exists("row_number.txt"):
            content = open("row_number.txt", 'r')
            row_number = content.readline()
            behavior_control['row'] = int(row_number)
            content.close()
            return int(row_number)
        else:
            self.show_error("Bitte eine Zeile nennen!")
        return 10000

    def row_changed(self, s):
        s = int(s)
        behavior_control['row'] = s
        row_number = open("row_number.txt", 'w')
        row_number.write(str(s))
        row_number.close()
        self.buttonNew.setEnabled(False)

    def check_or_update_credentials(self, hole_csv):
        self.permission = CheckPermissons(self.dialog, self.login)
        self.permission.signals.error.connect(self.show_error)
        self.permission.get_permissions()
        self.permission.signals.finished.connect(self.read_entries_from_csv)
        return

    def read_entries_from_csv(self):
        self.clear_ui()

        row_number = self.get_row_number()

        csv_path = os.path.join(os.getcwd(), "Anmeldung Kurs.csv")

        # header needs to match now broken csv (since row 2660)
        # tel line was deleted
        col_names = ["firstName", "lastName", "email", "institution", "personType", "courses",
                     "empty1", "empty2", "empty3", "empty4", "empty5", "empty6", "empty7"]

        hole_csv = pd.read_csv(csv_path, names=col_names)

        check_csv = hole_csv.iloc[0, 0]
        if check_csv != "firstName":
            self.check_or_update_credentials(hole_csv)
        else:
            print(f"Line output {check_csv}")
            len_list = len(hole_csv)
            print(f"This is line: {row_number} / {len_list}")

            if row_number >= len_list:
                self.show_error("Ende der Liste")
                self.automatic_continue.setChecked(False)
                self.readList.setEnabled(False)
                self.forward.setEnabled(False)
                behavior_control['read_from_list'] = False
                row_number = len_list
                self.row_changed(row_number)
            else:
                behavior_control['read_from_list'] = True

            self.row_field.setText(str(row_number))
            self.list_field.setText(str(len_list))

            # adjust row number to match the actual table
            row_number -= 1

            user['fname'] = hole_csv.at[row_number, 'firstName'].title().strip()
            self.fname.setText(user['fname'])

            user['lname'] = hole_csv.at[row_number, 'lastName'].title().strip()
            self.lname.setText(user['lname'])

            if str(hole_csv.at[row_number, 'institution']) != 'nan':
                user['facility'] = str(hole_csv.at[row_number, 'institution'])
                self.facility.setText(user['facility'])

            user['role'] = hole_csv.at[row_number, 'personType']
            self.role.setText(user['role'])

            # if str(hole_csv.at[row_number, 'tel']) != 'nan':
            #    user['telephone'] = str(hole_csv.at[row_number, 'tel'])
            #    self.telephone.setText(user['telephone'])

            user['mail'] = hole_csv.at[row_number, 'email']
            self.mail.setText(user['mail'])

            all_courses = hole_csv.at[row_number, 'courses']

            if pd.isnull(all_courses):
                self.show_error("Es wurden keine Kurse gewählt!")
            else:
                if 'Kundenservice' in all_courses:
                    user['kundenservice'] = 2
                    self.kundenservice.setChecked(True)
                if 'IT-Support' in all_courses:
                    user['it_support'] = 2
                    self.it_support.setChecked(True)
                if 'Grafikdesign' in all_courses:
                    user['grafikdesign'] = 2
                    self.grafikdesign.setChecked(True)
                if 'Diversity' in all_courses:
                    user['diversity'] = 2
                    self.diversity.setChecked(True)
                if 'Finanzanalyse' in all_courses:
                    user['finanzanalyse'] = 2
                    self.finanzanalyse.setChecked(True)
                if 'Digitaler Arbeitsplatz' in all_courses:
                    user['dig_arbeitsplatz'] = 2
                    self.dig_arbeitsplatz.setChecked(True)
                if 'IT-Administration' in all_courses:
                    user['it_administration'] = 2
                    self.it_administration.setChecked(True)
                if 'Projektmanagement' in all_courses:
                    user['projektmanagement'] = 2
                    self.projektmanagement.setChecked(True)
                if 'Digitales Marketing' in all_courses:
                    user['dig_marketing'] = 2
                    self.dig_marketing.setChecked(True)
                if 'Vertrieb und Verkauf' in all_courses:
                    user['vertrieb_verkauf'] = 2
                    self.vertrieb_verkauf.setChecked(True)
                if 'Soft Skills' in all_courses:
                    user['soft_skills'] = 2
                    self.soft_skills.setChecked(True)
                if 'Jobcoaching' in all_courses:
                    user['jobcoaching'] = 2
                    self.jobcoaching.setChecked(True)
                if 'Azure Fundamentals' in all_courses:
                    user['mc_af'] = 2
                    self.mc_af.setChecked(True)
                if 'Azure Data Fundamentals' in all_courses:
                    user['mc_adf'] = 2
                    self.mc_adf.setChecked(True)
                if 'Azure AI Fundamentals' in all_courses:
                    user['mc_aaf'] = 2
                    self.mc_aaf.setChecked(True)
                if 'Softwareentwicklung' in all_courses:
                    user['softwareentwicklung'] = 2
                    self.softwareentwicklung.setChecked(True)
                if 'Datenanalyse' in all_courses:
                    user['datenanalyse'] = 2
                    self.datenanalyse.setChecked(True)
                if 'Dynamics 365' in all_courses:
                    user['dynamics365'] = 2
                    self.dynamics.setChecked(True)
                if 'Microsoft 365' in all_courses:
                    user['microsoft365'] = 2
                    self.microsoft.setChecked(True)
                if 'Power Platform' in all_courses:
                    user['power_platform'] = 2
                    self.power_platform.setChecked(True)
                if 'Microsoft Teams' in all_courses:
                    user['teams'] = 2
                    self.teams.setChecked(True)
                    """ 
                    From here are Einstiegskurse 
                    (not shown in UI)
                    """
                if 'Netzwerke nutzen' in all_courses:
                    user['Netzwerke nutzen'] = 2
                if 'Bewerbung optimieren' in all_courses:
                    user['Bewerbung optimieren'] = 2
                if 'Kommunizieren via E-Mail' in all_courses:
                    user['Kommunizieren via E-Mail'] = 2
                if 'Jobsuche perfektionieren' in all_courses:
                    user['Jobsuche perfektionieren'] = 2
                if 'Selbstmanagement lernen' in all_courses:
                    user['Selbstmanagement lernen'] = 2
                if 'Kollaboration über Teams' in all_courses:
                    user['Kollaboration über Teams'] = 2

            self.buttonNew.setEnabled(True)
            self.readList.setEnabled(True)

    def clear_ui(self):
        user['fname'] = ''
        self.fname.setText(user['fname'])

        user['lname'] = ''
        self.lname.setText(user['lname'])

        user['facility'] = ''
        self.facility.setText(user['facility'])

        user['role'] = ''
        self.role.setText(user['role'])

        user['telephone'] = ''
        self.telephone.setText(user['telephone'])

        user['mail'] = ''
        self.mail.setText(user['mail'])

        user['kundenservice'] = ''
        self.kundenservice.setChecked(False)

        user['it_support'] = ''
        self.it_support.setChecked(False)

        user['grafikdesign'] = ''
        self.grafikdesign.setChecked(False)

        user['diversity'] = ''
        self.diversity.setChecked(False)

        user['finanzanalyse'] = ''
        self.finanzanalyse.setChecked(False)

        user['dig_arbeitsplatz'] = ''
        self.dig_arbeitsplatz.setChecked(False)

        user['it_administration'] = ''
        self.it_administration.setChecked(False)

        user['projektmanagement'] = ''
        self.projektmanagement.setChecked(False)

        user['dig_marketing'] = ''
        self.dig_marketing.setChecked(False)

        user['vertrieb_verkauf'] = ''
        self.vertrieb_verkauf.setChecked(False)

        user['soft_skills'] = ''
        self.soft_skills.setChecked(False)

        user['jobcoaching'] = ''
        self.jobcoaching.setChecked(False)

        user['mc_af'] = ''
        self.mc_af.setChecked(False)

        user['mc_adf'] = ''
        self.mc_adf.setChecked(False)

        user['mc_aaf'] = ''
        self.mc_aaf.setChecked(False)

        user['softwareentwicklung'] = ''
        self.softwareentwicklung.setChecked(False)

        user['datenanalyse'] = ''
        self.datenanalyse.setChecked(False)

        user['dynamics365'] = ''
        self.dynamics.setChecked(False)

        user['microsoft365'] = ''
        self.microsoft.setChecked(False)

        user['power_platform'] = ''
        self.power_platform.setChecked(False)

        user['teams'] = ''
        self.teams.setChecked(False)

    def button_toggle(self):
        user['toggled'] = not user['toggled']

        self.buttonNew.setText("Account erstellen") if user['toggled'] else self.buttonNew.setText(
            "Account wird erstellt ...")

        print("toggle is now: " + str(user['toggled']))

        self.buttonNew.setEnabled(user['toggled'])
