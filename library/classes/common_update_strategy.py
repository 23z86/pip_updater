import subprocess
from library.interfaces.update_strategy import IUpdateStrategy


class CommonUpdateStrategy(IUpdateStrategy):
    def run(self, package_name):
        subprocess.run(['pip', 'install', '--upgrade', package_name], check=True)
