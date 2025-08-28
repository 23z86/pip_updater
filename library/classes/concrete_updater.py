# pylint: disable=missing-docstring

import subprocess
from library.interfaces.updater_interface import UpdaterInterface


class ConcreteUpdater(UpdaterInterface):
    def run(self, **kwargs):
        package_name = kwargs.get('package_name')
        cmd = ['pip', 'install', '--upgrade', package_name]
        subprocess.run(cmd, check=True,
                       creationflags=subprocess.CREATE_NO_WINDOW)
