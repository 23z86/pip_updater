# pylint: disable=missing-docstring


import os
import re


class PackageReader():

    def run(self):
        pip_list = os.popen("pip list --outdated --format=json").read()
        return pip_list