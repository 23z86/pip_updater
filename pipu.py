import sys
import os
import subprocess
import re
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton
from PyQt6.QtCore import QThread, Qt
from PyQt6.QtGui import QIcon, QPixmap
from library.classes.pipu_main import PipUMain


class StartWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Your outdated PyPi-Modules")
        self.setFixedSize(440, 400)
        self.setWindowIcon(QIcon(QPixmap("logo.png")))

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        refresh_button = QPushButton("(Refresh)")
        # refresh_button.clicked.connect(self.refresh_table)
        self.o_pipu = PipUMain()

        self.pip_packages = self.o_pipu.read_package()

        self.table = QTableWidget(self)
        self.table.setRowCount(len(self.pip_packages))
        self.table.setColumnCount(4)
        self.table.resizeRowsToContents()
        self.table.setFixedWidth(450)

        self.table.setHorizontalHeaderLabels(
            ["Package Name", "Current Version", "Latest Version", "Update"])

        for row, row_data in enumerate(self.pip_packages):
            for col, item in enumerate(row_data):
                self.table.setItem(row, col, QTableWidgetItem(item))

            update_button = QPushButton("Update")
            update_button.clicked.connect(
                lambda _, row=row: self.run_update(row))
            self.table.setCellWidget(row, 3, update_button)

        self.table.resizeColumnsToContents()
        total_width = sum([self.table.columnWidth(i)
                          for i in range(self.table.columnCount())])
        vertical_header = self.table.verticalHeader()
        if vertical_header is not None:
            total_width += vertical_header.width() + 20
        else:
            total_width += 20
        self.table.setFixedWidth(total_width)

        layout.addWidget(refresh_button)
        layout.addWidget(self.table)

    def run_update(self, row):
        item = self.table.item(row, 0)

        if item is not None:
            self.o_pipu.finished.connect(self.on_update_finished)
            self.o_pipu.finished.connect(lambda: self._workers.remove(self.o_pipu))
            self.o_pipu.start()

            if not hasattr(self, "_workers"):
                self._workers = []
            

            self._workers.append(self.o_pipu)
            self.o_pipu.update_package(item.text())

    def on_update_finished(self):
        print("Update erfolgreich beendet!")
    # def refresh_table(self):
    #     class RefreshWorker(QThread):
    #         data_ready = pyqtSignal(list)

    #         def __init__(self, pipu):
    #             super().__init__()
    #             self.pipu = pipu

    #         def run(self):
    #             data = self.pipu.read_package()
    #             self.data_ready.emit(data)

    #     def update_table(data):
    #         self.table.setRowCount(0)
    #         self.table.setRowCount(len(data))
    #         self.table.setColumnCount(4)
    #         self.table.resizeRowsToContents()

    #         for row, row_data in enumerate(data):
    #             for col, item in enumerate(row_data):
    #                 self.table.setItem(row, col, QTableWidgetItem(item))
    #             update_button = QPushButton("Update")
    #             update_button.clicked.connect(
    #                 lambda _, row=row: self.run_update(row))
    #             self.table.setCellWidget(row, 3, update_button)

    #     worker = RefreshWorker(self.o_pipu)
    #     worker.data_ready.connect(update_table)
    #     worker.start()
    #     # Keep a reference to prevent garbage collection
    #     if not hasattr(self, "_refresh_workers"):
    #         self._refresh_workers = []
    #     self._refresh_workers.append(worker)
    #     worker.finished.connect(lambda: self._refresh_workers.remove(worker))


def main() -> None:
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = StartWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
