# pylint: disable=missing-docstring

from library.interfaces.subprocess_interface import SubprocessInterface
from library.classes.concrete_reader import ConcreteReader
from library.classes.concrete_updater import ConcreteUpdater
from library.classes.concrete_installer import ConcreteInstaller


class CommandFactory:
    def get_commander(self, subprocess_type) -> SubprocessInterface:
        valid_commands = {
            "read": ConcreteReader(), "update": ConcreteUpdater(), "install": ConcreteInstaller()}

        return valid_commands[subprocess_type]
