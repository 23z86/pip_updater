# pylint: disable=missing-docstring

import unittest


from doubles.fake_requests_runner import FakeRequestsRunner
from library.classes.concrete_checker import PackageChecker


class UpdateSubprocessTest(unittest.TestCase):
    def setUp(self) -> None:
        self.o_fake_requests = FakeRequestsRunner()
        self.o_checker = PackageChecker(self.o_fake_requests)

    def tearDown(self) -> None:
        del self.o_fake_requests
        del self.o_checker

    def test_valid_request_executed(self):
        package_name = "FakeRequests"

        self.o_fake_requests.set_request_ok(package_name)

        self.o_checker.run(package_name=package_name)
        self.o_fake_requests.execute(package_name=package_name)

    def test_invalid_request_executed(self):
        package_name = "FakeRequests"

        self.o_fake_requests.set_request_failed(package_name)

        try:
            self.o_fake_requests.execute(package_name=package_name)
        except ModuleNotFoundError as exception:
            self.assertEqual(exception.msg, "Package FakeRequests not found.")

    def test_invalid_request_leads_to_404(self):
        package_name = "FakeRequests"

        self.o_fake_requests.set_request_failed(package_name)

        self.assertEqual(self.o_fake_requests.status_code, 404)