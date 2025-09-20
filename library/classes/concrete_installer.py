# pylint: disable=missing-docstring

from library.interfaces.updater_interface import UpdaterInterface
from library.classes.install_subprocess import InstallSubprocess
from library.interfaces.subprocess_interface import SubprocessInterface


class ConcreteInstaller(UpdaterInterface):
    def __init__(self):
        self.o_subprocess_runner: SubprocessInterface = InstallSubprocess()

    def run(self, **kwargs):
        package_name = kwargs.get('package_name')
        self.o_subprocess_runner.run(package_name=package_name)
