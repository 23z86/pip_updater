# pylint: disable=missing-docstring


from library.interfaces.update_strategy import IUpdateStrategy


class PackageUpdater():

    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: IUpdateStrategy):
        self.strategy = strategy

    def update(self, package_name=None):
        assert self.strategy is not None, "Update strategy not set. Call set_strategy() before update()."
        self.strategy.run(package_name=package_name)
