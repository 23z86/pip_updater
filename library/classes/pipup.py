# pylint: disable=missing-docstring


from library.interfaces.reader_interface import ReaderInterface
from library.interfaces.updater_interface import UpdaterInterface


class PipUp:
    def __init__(self, reader: ReaderInterface, updater: UpdaterInterface):
        self.o_reader = reader
        self.o_updater = updater

    def update_package(self, package_name):
        self.o_updater.run(package_name=package_name)

    def read_outdated_packages(self):
        return self.o_reader.run()
