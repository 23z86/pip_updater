# pylint: disable=missing-docstring
from library.interfaces.reader_interface import ReaderInterface

import subprocess
import json


class ConcreteReader(ReaderInterface):

    def run(self):
        raw_pip_list = subprocess.run(
            ["pip", "list", "--outdated", "--format=json"],
            capture_output=True,
            text=True,
            check=True, creationflags=subprocess.CREATE_NO_WINDOW
        )

        pip_list = json.loads(raw_pip_list.stdout)
        return pip_list
