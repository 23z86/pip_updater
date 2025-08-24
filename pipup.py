# pylint: disable=missing-docstring


from library.classes.package_updater import PackageUpdater
from library.classes.common_update_strategy import CommonUpdateStrategy
from library.classes.pip_update_strategy import PipUpdateStrategy
from library.classes.package_reader import PackageReader


class PipUp:
    def __init__(self):
        self.updater = PackageUpdater()
        self.o_reader = PackageReader()

    def update_package(self, package_name):
        self.updater.set_strategy(
            PipUpdateStrategy() if package_name == "pip" else CommonUpdateStrategy()
        )
        self.updater.update(package_name)

    def read_outdated_packages(self):
        return self.o_reader.run()
