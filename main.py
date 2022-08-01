####!/Users/ben/.virtualenvs/IS-Table/bin/python
#!/Users/ben/Library/Caches/pypoetry/virtualenvs/accountmanager-lWHTfMHr-py3.9/bin/python

####!~/.virtualenvs/IS-Table/bin/python

# /home/ben/.pyenv/shims/python3
# ignores venv on macos

# pyside6-uic mainwindow.ui -o MainWindow.py && ./main.py
# pyside6-uic mainwindow.ui -o MainWindow.py && pyside6-uic dialogwindow.ui -o DialogWindow.py && ./main.py
# pyside6-uic mainwindow.ui -o MainWindow.py && pyside6-uic dialogwindow.ui -o DialogWindow.py

try:
    from PySide6.QtWinExtras import QtWin
    appid = 'de.47q.matrix.accountmanager.v0.1'
    QtWin.setCurrentProcessExplicitAppUserModelID(appid)
except ImportError:
    pass

import sys

from PySide6.QtWidgets import QApplication

from gui import MainWindow

from PySide6 import QtGui

app = QApplication(sys.argv)
#app = QApplication()
app.setStyle('Fusion')
app.setWindowIcon(QtGui.QIcon('happy.ico'))
window = MainWindow()
window.show()

app.exec()
