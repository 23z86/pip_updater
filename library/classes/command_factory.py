# pylint: disable=missing-docstring

from library.interfaces.subprocess_interface import SubprocessInterface
from library.classes.concrete_reader import ConcreteReader
from library.classes.concrete_updater import ConcreteUpdater


class CommandFactory:
    def get_commander(self, subprocess_type) -> SubprocessInterface:
        valid_subprocesses = {
            "read": ConcreteReader(), "update": ConcreteUpdater()}

        return valid_subprocesses[subprocess_type]
