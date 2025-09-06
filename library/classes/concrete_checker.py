# pylint: disable=missing-docstring


from library.interfaces.checker_interface import CheckerInterface
from library.interfaces.requests_interface import RequestsInterface


class PackageChecker(CheckerInterface):
    def __init__(self, runner: RequestsInterface):
        self.o_runner = runner

    def run(self, **kwargs):
        package_name = kwargs.get('package_name')

        self.o_runner.execute(package_name=package_name)
