# pylint: disable=missing-docstring


from library.classes.concrete_reader import ConcreteReader
from library.classes.concrete_updater import ConcreteUpdater



class PipUp:
    def __init__(self):
        self.o_reader = ConcreteReader()
        self.o_updater = ConcreteUpdater()

    def update_package(self, package_name):
        self.o_updater.run(package_name=package_name)

    def read_outdated_packages(self):
        return self.o_reader.run()
