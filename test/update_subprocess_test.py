# pylint: disable=missing-docstring

import unittest


from doubles.fake_update_subprocess import FakeUpdateSubprocess
from library.classes.update_subprocess import UpdateSubprocess


class UpdateSubprocessTest(unittest.TestCase):
    def setUp(self) -> None:
        self.o_fake_subprocess_runner = FakeUpdateSubprocess()
        self.o_updater = UpdateSubprocess(self.o_fake_subprocess_runner)

    def tearDown(self) -> None:
        del self.o_fake_subprocess_runner
        del self.o_updater

    def test_correct_package_used(self):
        package_name = "FakeFlask"
        self.o_updater.run(package_name=package_name)
        self.assertTrue(self.o_fake_subprocess_runner.expect_called_with_package(
            package_name=package_name), f"Package name should be {package_name}.")

    def test_versions_differ(self):
        package_name = "FakeFlask"
        self.o_updater.run(package_name=package_name)
        self.assertTrue(self.o_fake_subprocess_runner.expect_version_differs(
        ), "Old version and new version should be different")

    def test_versions_are_equal(self):
        package_name = "FakeFlask"
        self.o_updater.run(package_name=package_name)
        self.assertTrue(self.o_fake_subprocess_runner.expect_no_update_needed(
        ), "Versions should be 1.3.3.7")
