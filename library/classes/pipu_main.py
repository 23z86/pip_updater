from PyQt6.QtCore import QThread
from PyQt6.QtCore import pyqtSignal
from library.classes.common_update_strategy import CommonUpdateStrategy
from library.classes.pip_update_strategy import PipUpdateStrategy
from library.classes.update_worker import UpdateWorker
from library.classes.package_reader import PackageReader


class PipUMain(QThread):
    finished = pyqtSignal()

    def __init__(self):
        self.o_reader = PackageReader()
        self.o_updater = UpdateWorker()
        self.o_updater.set_strategy(CommonUpdateStrategy())

    def read_package(self):
        return self.o_reader.read_outdated_packages()

    def update_package(self, package_name):
        self.o_updater.update(package_name)
        self.finished.emit()

    def update_pip(self):
        self.o_updater.reset_strategy()
        self.o_updater.set_strategy(PipUpdateStrategy())
        self.o_updater.update()
