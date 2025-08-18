# pylint: disable=missing-docstring


import subprocess
import json


class PackageReader():

    def run(self):
        raw_pip_list = subprocess.run(
            ["pip", "list", "--outdated", "--format=json"],
            capture_output=True,
            text=True,
            check=True
        )

        pip_list = json.loads(raw_pip_list.stdout)
        return pip_list
