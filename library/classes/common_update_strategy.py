# pylint: disable=missing-docstring

import subprocess
from library.interfaces.update_strategy import IUpdateStrategy


class CommonUpdateStrategy(IUpdateStrategy):
    def run(self, **kwargs):
        package_name = kwargs.get('package_name')
        cmd = ['python', '-m', 'pip', 'install', '--upgrade', package_name]
        subprocess.run(cmd, check=True,
                       creationflags=subprocess.CREATE_NO_WINDOW)
