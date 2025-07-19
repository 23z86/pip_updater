from unittest import TestCase
from library.classes.package_reader import PackageReader

class PackageReaderTest(TestCase):
    def setUp(self) -> None:
        self.package_reader = PackageReader()

    def tearDown(self) -> None:
        del self.package_reader

    def test_get_installed_packages(self):
        installed_packages = self.package_reader.run()
        self.assertIsInstance(installed_packages, list)
        self.assertGreater(len(installed_packages), 0)