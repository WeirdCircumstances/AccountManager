import os

from PySide6.QtWidgets import (
    QWidget,
)

from PySide6.QtCore import QRunnable

from DialogWindow import Ui_DialogWindow

from signals import WorkerSignals

import json


class NeedPermissions(QWidget, Ui_DialogWindow):
    def __init__(self, login, *args, obj=None, **kwargs):
        super(NeedPermissions, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.signals = WorkerSignals()
        # self.show()

        self.login = login

        self.name = ""
        self.passwd = ""

        self.nameBox.setText("Login für " + login)

        self.nameLine.textEdited.connect(self.name_changed)
        self.passwdLine.textEdited.connect(self.passwd_changed)

        self.dialogBox.accepted.connect(self.accept)
        self.dialogBox.rejected.connect(self.reject)

    def name_changed(self, s):
        self.name = s
        print(s)
        # self.signals.result.emit({"name_" + self.login: s})

    def passwd_changed(self, s):
        self.passwd = s
        print(s)

    def accept(self):
        print("ok")
        self.signals.result.emit({
            "name_" + self.login: self.name,
            "passwd_" + self.login: self.passwd
        })
        self.close()

    def reject(self):
        print("cancel")
        self.close()


def read_json():
    if os.path.exists("credentials.json"):
        with open('credentials.json') as json_file:
            data = json.load(json_file)
    else:
        data = {}

    return data


def write_json(data):
    with open('credentials.json', 'w') as outfile:
        json.dump(data, outfile)
    print(data)


class CheckPermissons(QRunnable):

    def __init__(self, dialog, login):
        super().__init__()

        self.signals = WorkerSignals()

        self.dialog = dialog

        self.login = login

    def check(self):
        data = read_json()

        if "name_" + self.login in data:
            return True
        else:
            self.get_permissions()

    def get_permissions(self):
        if self.dialog is None:
            self.dialog = NeedPermissions(self.login)
            self.dialog.signals.result.connect(self.process_json)
            self.dialog.show()
            # time.sleep(10)
        else:
            print("there is already a window")

    def process_json(self, s):
        data = read_json()

        data.update(s)

        write_json(data)
        self.signals.error.emit("Daten wurden gespeichert")
