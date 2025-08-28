# pylint: disable=missing-docstring

from library.interfaces.checker_interface import CheckerInterface
from importlib import util


class PackageChecker(CheckerInterface):
    def run(self, **kwargs):
        package_name = kwargs.get('package_name')
        
        #TODO build a request to pypi website to check whether the package is exisiting. More reliable
        if not util.find_spec(package_name):
            raise ModuleNotFoundError(
                f"Package {package_name} not found or is not installed.")
