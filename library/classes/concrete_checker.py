# pylint: disable=missing-docstring

from library.interfaces.checker_interface import CheckerInterface
import requests


class PackageChecker(CheckerInterface):
    def run(self, **kwargs):
        package_name = kwargs.get('package_name')

        response = requests.get(f'https://pypi.org/pypi/{package_name}/json')

        if response.status_code == 404:
            raise ModuleNotFoundError(
                f"Package {package_name} not found.")
