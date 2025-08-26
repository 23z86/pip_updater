
import subprocess
import json
from library.interfaces.subprocess_interface import SubprocessInterface


class SubprocessRunner(SubprocessInterface):
    def __init__(self, runner=None):
        self.runner = runner or subprocess

    def run(self):
        raw_pip_list = self.runner.run(
            ["pip", "list", "--outdated", "--format=json"],
            capture_output=True,
            text=True,
            check=True, creationflags=subprocess.CREATE_NO_WINDOW
        )
        pip_list = json.loads(raw_pip_list.stdout)

        return pip_list
