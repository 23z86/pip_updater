from interfaces.update_strategy import IUpdateStrategy


class UpdateWorker():

    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: IUpdateStrategy):
        self.strategy = strategy

    def reset_strategy(self):
        self.strategy = None

    def update(self, package_name=None):
        self.strategy.run(package_name)
