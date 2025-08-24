# pylint: disable=missing-docstring


from library.classes.common_update_strategy import CommonUpdateStrategy
from library.classes.pip_update_strategy import PipUpdateStrategy
from library.interfaces.update_strategy import IUpdateStrategy


class UpdateFactory:
    def get_strategy(self, package_name: str) -> IUpdateStrategy:
        if package_name == "pip":
            return PipUpdateStrategy()

        return CommonUpdateStrategy()
