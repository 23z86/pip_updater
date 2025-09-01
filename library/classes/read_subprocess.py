
import subprocess
import json
from library.interfaces.subprocess_interface import SubprocessInterface


class ReadSubprocess(SubprocessInterface):
    def __init__(self, runner=None):
        self.runner = runner or subprocess

    def run(self):
        command =   ["pip", "list", "--outdated", "--format=json"]
        raw_pip_list = self.runner.run(
            command,
            capture_output=True,
            text=True,
            check=True, creationflags=subprocess.CREATE_NO_WINDOW
        )
        pip_list = json.loads(raw_pip_list.stdout)

        return pip_list
