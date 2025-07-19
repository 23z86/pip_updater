# pylint: disable=missing-docstring


import os
import re


class PackageReader():

    def run(self):
        raw_pip_list = os.popen("pip list --outdated").read()
        raw_pip_list_no_header = raw_pip_list.splitlines()[2:]
        package_info = []

        for entry in raw_pip_list_no_header:
            match = re.match(r"^([^\s]+)\s+([^\s]+)\s+([^\s]+)", entry)
            if match:
                package_info.append(match.groups())

        return package_info
