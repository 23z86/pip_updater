# pylint: disable=missing-docstring

from library.interfaces.updater_interface import UpdaterInterface
from library.interfaces.subprocess_interface import SubprocessInterface


class ConcreteUpdater(UpdaterInterface):
    def __init__(self, o_subprocess_runner: SubprocessInterface):
        self.o_subprocess_runner = o_subprocess_runner

    def run(self, **kwargs):
        package_name = kwargs.get('package_name')
        self.o_subprocess_runner.run(package_name=package_name)
