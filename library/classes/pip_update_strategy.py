# pylint: disable=missing-docstring


import subprocess
from library.interfaces.update_strategy import IUpdateStrategy


class PipUpdateStrategy(IUpdateStrategy):
    def run(self, **kwargs):
        pip_package = kwargs.get('package_name')
        cmd = ['python', '-m', 'pip', 'install', '--upgrade', pip_package]
        subprocess.run(cmd, check=True,
                       creationflags=subprocess.CREATE_NO_WINDOW)
