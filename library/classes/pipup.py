# pylint: disable=missing-docstring

from library.classes.subprocess_factory import SubprocessFactory
from library.classes.concrete_reader import ConcreteReader
from library.classes.concrete_updater import ConcreteUpdater


class PipUp:
    def __init__(self):
        self.o_factory = SubprocessFactory()

    def update_package(self, package_name):
        o_update_subprocess = self.o_factory.get_subprocess("update")
        o_updater = ConcreteUpdater(o_update_subprocess)

        o_updater.run(package_name=package_name)

    def read_outdated_packages(self):
        o_read_subprocess = self.o_factory.get_subprocess("read")
        o_reader = ConcreteReader(o_read_subprocess)

        return o_reader.run()
