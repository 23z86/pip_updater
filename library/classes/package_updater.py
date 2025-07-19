# pylint: disable=missing-docstring


from library.interfaces.update_strategy import IUpdateStrategy


class PackageUpdater():

    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: IUpdateStrategy):
        self.strategy = strategy

    def update(self, package_name=None):
        self.strategy.run(package_name)
