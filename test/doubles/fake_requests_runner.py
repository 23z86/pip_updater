# pylint: disable=missing-docstring

from library.interfaces.requests_interface import RequestsInterface


class FakeRequestsRunner(RequestsInterface):
    def __init__(self):
        self.status_code = None
        self.url = None
        self.reason = None

    def set_request_ok(self, package_name):
        self.status_code = 200
        self.url = f'https://pypi.org/pypi/{package_name}/json'
        self.reason = 'OK'

    def set_request_failed(self, package_name):
        self.status_code = 404
        self.url = f'https://pypi.org/pypi/{package_name}/json'
        self.reason = 'Not found.'

    def execute(self, **kwargs):
        package_name = kwargs.get('package_name')


        if self.status_code == 404:
            raise ModuleNotFoundError(
                f"Package {package_name} not found.")
