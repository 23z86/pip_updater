# pylint: disable=missing-docstring

import subprocess
from library.interfaces.subprocess_interface import SubprocessInterface


class UpdateSubprocess(SubprocessInterface):
    def __init__(self, runner=None):
        self.runner = runner or subprocess

    def run(self, **kwargs):
        package_name = kwargs.get("package_name")

        if package_name == "pip":
            command = ["python", "-m", "pip", "install", "--upgrade", package_name]

        command = ["pip", "install", "--upgrade", package_name]

        self.runner.run(command, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
