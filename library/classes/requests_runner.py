# pylint: disable=missing-docstring

import requests

from library.interfaces.requests_interface import RequestsInterface


class RequestsRunner(RequestsInterface):
    def __init__(self, requester=None):
        self.requester = requester or requests
        
    def execute(self, **kwargs):
        package_name = kwargs.get('package_name')

        response = self.requester.get(f'https://pypi.org/pypi/{package_name}/json')

        if response.status_code == 404:
            raise ModuleNotFoundError(
                f"Package {package_name} not found.")
        