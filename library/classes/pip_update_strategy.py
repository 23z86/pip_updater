import subprocess
from library.interfaces.update_strategy import IUpdateStrategy


class PipUpdateStrategy(IUpdateStrategy):
    def run(self, package_name=None):
        subprocess.run(['python', '-m', 'pip', 'install',
                       '--upgrade', 'pip'], check=True)
