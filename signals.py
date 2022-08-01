from PySide6.QtCore import (
    Signal,
    QObject
)


class WorkerSignals(QObject):
    progress = Signal(int)
    finished = Signal()
    error = Signal(str)
    result = Signal(dict)
