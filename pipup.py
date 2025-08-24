# pylint: disable=missing-docstring


from library.classes.package_updater import PackageUpdater
from library.classes.package_reader import PackageReader
from library.classes.update_factory import UpdateFactory


class PipUp:
    def __init__(self):
        self.o_updater = PackageUpdater()
        self.o_reader = PackageReader()
        self.o_factory = UpdateFactory()

    def update_package(self, package_name):
        strategy = self.o_factory.get_strategy(package_name)
        self.o_updater.set_strategy(strategy)
        self.o_updater.update(package_name)

    def read_outdated_packages(self):
        return self.o_reader.run()
