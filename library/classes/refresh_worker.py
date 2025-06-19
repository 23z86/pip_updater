from PyQt6.QtCore import QThread, pyqtSignal, QObject


class RefreshWorker(QThread):
    data_ready = pyqtSignal(list)

    def __init__(self, pipu):
        super().__init__()
        self.pipu = pipu

    def run(self):
        data = self.pipu.read_package()
        self.data_ready.emit(data)
