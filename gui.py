# pylint: disable=missing-docstring


from PyQt6.QtWidgets import QMainWindow, QWidget, QTableWidget, QVBoxLayout
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QApplication, QPushButton
import sys
import json

from library.classes.package_reader import PackageReader

class TableWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Table Example")
        self.setFixedSize(600, 400)
        self.o_package_reader = PackageReader()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        table = QTableWidget(self)
        table_data = self.o_package_reader.run()

        table.setRowCount(len(table_data))
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels([
            "Package", "Version", "Latest", "Action"
        ])
        json_data = json.loads(table_data)

        for row, pkg in enumerate(json_data):
            table.setItem(row, 0, QTableWidgetItem(pkg["name"]))
            table.setItem(row, 1, QTableWidgetItem(pkg["version"]))
            table.setItem(row, 2, QTableWidgetItem(pkg["latest_version"]))
            table.setItem(row, 3, QTableWidgetItem(QPushButton("Update").text()))

        layout.addWidget(table)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableWindow()
    window.show()
    sys.exit(app.exec())
