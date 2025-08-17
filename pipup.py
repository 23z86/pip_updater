# pylint: disable=missing-docstring


from library.classes.package_updater import PackageUpdater
from library.classes.common_update_strategy import CommonUpdateStrategy
from library.classes.pip_update_strategy import PipUpdateStrategy


class PipUp:
    def __init__(self, package_name):
        self.package_name = package_name
        self.updater = PackageUpdater()

    def update_pip(self):
        self.updater.set_strategy(PipUpdateStrategy())
        self.updater.update(self.package_name)

    def update_common(self):
        self.updater.set_strategy(CommonUpdateStrategy())
        self.updater.update(self.package_name)