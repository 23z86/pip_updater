# pylint: disable=missing-docstring

from library.classes.command_factory import CommandFactory


class PipUp:
    def __init__(self):
        self.o_factory = CommandFactory()

    def update_package(self, package_name):
        o_updater = self.o_factory.get_commander("update")
        o_updater.run(package_name=package_name)

    def read_outdated_packages(self):
        o_reader = self.o_factory.get_commander("read")
        return o_reader.run()
