import subprocess
import time
from csv import writer

from PySide6.QtCore import (
    QRunnable,
    QThreadPool,
    Slot
)

from userdata import user, behavior_control
from web import WorkerSignals

"""
Toolbox

status, output = subprocess.getstatusoutput('brew update')

az account show

az ad user create --display-name "Test Test" --password Abc12345 \
--user-principal-name it.test1@innovative-students.de --force-change-password-next-login true
az ad user get-member-groups --id it.test1@innovative-students.de

az ad group list --display-name "Digitales Marketing"

az ad user list --filter "displayname eq 'test test'"
az ad user show --id "it.test1@innovative-students.de" --query "objectId" --output tsv

az ad group member add --group Test --member-id 5f634584-87fe-407e-ba31-22871f54f8b7


az ad user create --display-name "Test Test" --password Abc12345 \
--user-principal-name it.test1@innovative-students.de --force-change-password-next-login true
az ad group member add --group Empfang --member-id $(az ad user show \
--id "it.test1@innovative-students.de" --query "objectId" --output tsv)
az ad group member check --group Empfang --member-id $(az ad user show \
--id "it.test1@innovative-students.de" --query "objectId" --output tsv) --query "value" --output tsv
"""


class ADWorker(QRunnable):

    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()

    def show_error(self, error):
        self.signals.error.emit(error)

    def generate_progress(self, progress):
        self.signals.progress.emit(progress)

    @Slot()
    def run(self):

        row_content = [''] * 40

        def login():
            status, output = subprocess.getstatusoutput("az account show")
            # print(output)

            self.signals.progress.emit(5)

            error_handler(status, output)

            self.signals.progress.emit(10)

            registration()
            return

        def registration():
            row_content[0] = user['fname']
            row_content[1] = user['lname']
            row_content[2] = user['facility']
            row_content[3] = ''
            row_content[4] = ''
            row_content[5] = user['role']
            row_content[6] = str(user['telephone'])
            row_content[7] = user['mail']
            row_content[8] = user['uid'].replace(".", "")

            displayName = user['fname'] + " " + user['lname']
            # print(displayName)
            password = user['passwd']
            print(password)
            domain = "@innovative-students.de"
            user['principalName'] = user['it_mail'] + domain
            print(user['principalName'])
            forceChangePasswd = "true"

            status, output = subprocess.getstatusoutput(
                "az ad user create \
                --display-name '{}' \
                --password '{}' \
                --user-principal-name '{}' \
                --force-change-password-next-sign-in '{}'".format(displayName, password, user['principalName'], forceChangePasswd))

            error_handler(status, output)

            if status == 0:
                self.signals.error.emit("Konto angelegt")
                print("Account created")
                self.signals.progress.emit(20)
                row_content[9] = user['it_mail'] + domain
                row_content[10] = user['passwd']

                addLicense()
                return
            else:
                self.signals.error.emit("Konto existiert bereits: Prüfe Lizenz ...")
                print("Account existing.")
                print(status, output)
                # print("Account existing, checking license.")
                row_content[9] = "Email wird bereits verwendet"
                row_content[10] = "versuche neue Gruppe(n) zuzuweisen"
                addLicense()
                # print(output)
                return

            # print(row_content)

        # Adds licence to this account.
        # Documentation:
        # https://docs.microsoft.com/en-us/azure/active-directory/enterprise-users/licensing-groups-assign

        def addLicense():
            # Deprecated. Licence is now managed by the group Empfang.

            # status, output = subprocess.getstatusoutput(
            #     "az ad user show --id '{}' --query assignedLicenses \
            #     --output tsv 2>nul".format(user['principalName']))
            # if output == "":
            #     # status, output = subprocess.getstatusoutput(
            #     #    "az ad user show --id '{}' --query objectId --output tsv 2>nul".format(user['principalName']))
            #     status, output = subprocess.getstatusoutput(
            #         "az ad user show --id '{}' --query id --output tsv 2>nul".format(user['principalName']))
            #     print("OBJECT ID")
            #     print(output)
            #     user['objectID'] = output
            #
            #     self.signals.error.emit("Füge Lizenz hinzu.")
            #     print("add license...")
            #     self.threadpool = QThreadPool()
            #     licenseRunner = WebHelper()
            #     # self.threadpool.start(licenseRunner)
            #     licenseRunner.signals.progress.connect(self.generate_progress)
            #     # self.show_error("")
            #     licenseRunner.signals.error.connect(self.show_error)
            #
            #     # licenseRunner.run()
            #
            # else:
            #     self.signals.error.emit("✅ Lizenz zugewiesen")
            #     print("License found, going to group setup")

            addGroups()
            return

        def addGroups():
            group_list = []

            if user['empfang'] == 2:
                group_list.append("Empfang")
                row_content[11] = 'x'
            if user['license'] == 2:
                group_list.append("License")
            if user['kundenservice'] == 2:
                group_list.append("Kundenservice")
                row_content[12] = 'x'
            if user['it_support'] == 2:
                group_list.append("IT-Support")
                row_content[13] = 'x'
            if user['grafikdesign'] == 2:
                group_list.append("Grafikdesign")
                row_content[14] = 'x'
            if user['diversity'] == 2:
                group_list.append("Diversity")
                row_content[15] = 'x'
            if user['finanzanalyse'] == 2:
                group_list.append("Finanzanalyse")
                row_content[16] = 'x'
            if user['dig_arbeitsplatz'] == 2:
                group_list.append("Digitaler Arbeitsplatz")
                row_content[17] = 'x'
            if user['it_administration'] == 2:
                group_list.append("IT-Administration")
                row_content[18] = 'x'
            if user['projektmanagement'] == 2:
                group_list.append("Projektmanagement")
                row_content[19] = 'x'
            if user['dig_marketing'] == 2:
                group_list.append("Digitales Marketing")
                row_content[20] = 'x'
            if user['mc_adf'] == 2:
                group_list.append("Azure Data")
                row_content[21] = 'x'
            if user['vertrieb_verkauf'] == 2:
                group_list.append("Vertrieb")
                row_content[22] = 'x'
            if user['mc_af'] == 2:
                group_list.append("Azure")
                row_content[23] = 'x'
            if user['soft_skills'] == 2:
                group_list.append("Soft Skills")
                row_content[24] = 'x'
            if user['jobcoaching'] == 2:
                group_list.append("Jobsuche")
                row_content[25] = 'x'
            if user['mc_aaf'] == 2:
                group_list.append("Azure AI")
                row_content[26] = 'x'
            if user['softwareentwicklung'] == 2:
                group_list.append("Softwareentwicklung")
                row_content[27] = 'x'
            if user['datenanalyse'] == 2:
                group_list.append("Datenanalyse")
                row_content[28] = 'x'
            if user['dynamics365'] == 2:
                group_list.append("Dynamics 365")
                row_content[29] = 'x'
            if user['microsoft365'] == 2:
                group_list.append("Microsoft 365")
                row_content[30] = 'x'
            if user['power_platform'] == 2:
                group_list.append("Power Platform")
                row_content[31] = 'x'
            if user['teams'] == 2:
                group_list.append("Microsoft Teams")
                row_content[32] = 'x'
            if user['Netzwerke nutzen'] == 2:
                row_content[33] = 'x'
            if user['Bewerbung optimieren'] == 2:
                row_content[34] = 'x'
            if user['Kommunizieren via E-Mail'] == 2:
                row_content[35] = 'x'
            if user['Jobsuche perfektionieren'] == 2:
                row_content[36] = 'x'
            if user['Selbstmanagement lernen'] == 2:
                row_content[37] = 'x'
            if user['Kollaboration über Teams'] == 2:
                row_content[38] = 'x'
            else:
                self.signals.error.emit("❌ Keine Gruppen ausgewählt!")

            self.signals.progress.emit(60)

            self.signals.error.emit("Es werden " + str(len(group_list)) + " Gruppen zugewiesen.")

            def check_status(gp, uid):
                status, output = subprocess.getstatusoutput(
                    "az ad group member check --group '{}' --member-id '{}' --query 'value' --output tsv 2>nul".format(gp, uid)
                )
                print(output + ": " + gp)
                return output

            def get_object_ID():
                # status, output = subprocess.getstatusoutput(
                #    "az ad user show --id '{}' --query objectId --output tsv 2>nul".format(user['principalName']))
                status, output = subprocess.getstatusoutput(
                    "az ad user show --id '{}' --query id --output tsv 2>nul".format(user['principalName']))
                # print("OBJECT ID")
                # print(output)
                return output

            user_id = get_object_ID()
            print("UserID: " + str(user_id))

            def add_to_group(gp, uid):
                status, output = subprocess.getstatusoutput(
                    "az ad group member add --group '{}' --member-id '{}' --query 'value' --output tsv 2>nul".format(gp, uid)
                )
                return status

            list_length = len(group_list)

            for nr, group in enumerate(group_list):
                # if check_status(entry, user_id) == "false":
                status = add_to_group(group, user_id)

                if status == 0:
                    self.signals.error.emit("✅ " + group + " hinzugefügt.")
                    self.signals.progress.emit(60 + (38 * ((nr + 1) / list_length)))
                    print("new: " + group)
                    # time.sleep(0.4)

                else:
                    self.signals.progress.emit(60 + (38 * ((nr + 1) / list_length)))
                    self.signals.error.emit("👍 " + group + " vorhanden")
                    # time.sleep(1)

                # status, output = subprocess.getstatusoutput(
                #     "az ad group member check --group '{}' --member-id {}".format(entry, user['objectID'])
                # )
                # print("Is member of group: " + output)

                # time.sleep(1)  # not to fast

            time.sleep(0.2)
            write_and_close()
            return

        def write_and_close():
            self.signals.progress.emit(99)
            self.signals.error.emit("Schreibe csv...")

            write_csv()
            time.sleep(0.2)  # slow enough to read output

            self.signals.progress.emit(100)
            # self.signals.error.emit("✅ Fertig!")
            return

        def append_list_as_row(file_name, row_content):
            # Open file in append mode
            with open(file_name, encoding='utf-8', mode='a+', newline='') as write_obj:
                # Create a writer object from csv module
                csv_writer = writer(write_obj)
                # Add contents of list as last row in the csv file
                csv_writer.writerow(row_content)
            return

        def write_csv():
            append_list_as_row('newAccounts.csv', row_content)
            increase_row_by_one()

        def get_row_number():
            row_number = open("row_number.txt", encoding='utf-8', mode='r')
            content = row_number.readline()
            row_number.close()
            return content

        def increase_row_by_one():
            if behavior_control['read_from_list']:
                row_number = int(get_row_number())
                # behavior_control['row']
                row_number += 1

                row_text_file = open("row_number.txt", encoding='utf-8', mode='w')
                row_text_file.write(str(row_number))
                row_text_file.close()
                behavior_control['row'] = int(row_number)
                print("New row number: ")
                behavior_control['read_from_list'] = False
                print(row_number)

        def error_handler(status, output):

            if 'expired' in output:
                status, output = subprocess.getstatusoutput("az logout")
                print("There was an error, user should login again.")
                self.signals.error.emit("Das Passwort war abgelaufen. Bitte neu einloggen")
                print("Change password in web class.")
                time.sleep(30)
                login()
                return

            if 'to setup account' in output:
                status, output = subprocess.getstatusoutput("az login")
                self.signals.error.emit("Bitte im Browser für Azure Cloud Shell einloggen")
                time.sleep(3)
                print("Not logged in, return...")

                login()
                # self.signals.error.emit("✅ Login erfolgreich")
                return

            if 'ERROR' in output:
                print(status, output)
                if 'value for property userPrincipalName' in output:
                    pass
                else:
                    while 1:
                        self.signals.error.emit(str(status) + ", " + output)
                        time.sleep(10)
                        self.signals.error.emit("Es ist ein Fehler aufgetreten:")

            if status == 127:
                self.signals.error.emit("❌ Ist Azure CLI installiert?")
                print("Can not find Azure Cloud Shell ...")
                print(output)
                for i in range(5):
                    self.signals.error.emit("❌ Ist Azure CLI installiert?")
                    time.sleep(3)
                    self.signals.error.emit("❌ Bitte Azure CLI installieren!")
                    time.sleep(3)
                    self.signals.error.emit("❌ oder neu einloggen mit \"az login\"")
                    time.sleep(3)
                    self.signals.error.emit("❌ oder die Python Umgebung neu starten")
                    time.sleep(3)

                return
                # sys.exit()

        login()


class ADmanage(QRunnable):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.signals = WorkerSignals()

        # self.search

    def show_error(self, error):
        self.signals.error.emit(error)

    def generate_progress(self, progress):
        self.signals.progress.emit(progress)

    @Slot()
    def search(self, search):
        # search for Accounts

        user['principalName'] = ''
        print(search)

        status, output = subprocess.getstatusoutput(
            f"az ad user list --filter \"startswith(displayName, '{search}') or \
            startswith(userPrincipalName, '{search}')\" \
            --query \"[].userPrincipalName\" \
            --output tsv \
            2>nul ")

        output_length = len(output)

        if (1 < output_length < 50) & ('@' in output):
            self.signals.error.emit("Gültige Emailadresse erkannt: \n \n" + output)
            user['principalName'] = output
        elif search == '':
            self.signals.error.emit("Zuerst einen Suchbegriff eingeben.")
        else:
            self.signals.error.emit(output)

        print(len(output))
        print("output: " + output)

    def set_passwd(self, passwd):

        if user['principalName'] != '':

            if user['tmp_passwd'] == 2:
                force_change_passwd = "true"
            else:
                force_change_passwd = "false"

            status, output = subprocess.getstatusoutput(
                f"az ad user update \
                --id {user['principalName']} \
                --force-change-password-next-login {force_change_passwd} \
                --password \'{passwd}\' \
            ")

            self.signals.error.emit(
                user['principalName'] + "\n" +
                passwd + "\n" + "\n" +
                "Adresse: " + user['principalName'] + "\n" +
                "Passwort: " + passwd + "\n" + "\n" +
                "Temporäres Passwort: " + force_change_passwd + "\n" + "\n" +
                output
            )

        else:
            self.signals.error.emit("Kein Nutzer angegeben.")

    def delete_account(self, uid):
        # print("not implemented")

        if user['principalName'] != '':
            status, output = subprocess.getstatusoutput(
                f"az ad user delete --id {user['principalName']} 2>nul")

            if status == 0:
                self.signals.error.emit(user['principalName'] + " erfolgreich gelöscht.")
            else:
                self.signals.error.emit(output)

            print(status)
        else:
            self.signals.error.emit("Kein Nutzer angegeben.")
