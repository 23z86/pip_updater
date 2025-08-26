import unittest

from mocks.fake_reader import FakeReader
from mocks.dummy_updater import DummyUpdater
from library.classes.pipup import PipUp


class PipUpTest(unittest.TestCase):
    def setUp(self) -> None:
        self.o_fake_reader = FakeReader()
        self.o_pipup = PipUp(self.o_fake_reader, DummyUpdater())

    def tearDown(self) -> None:
        del self.o_pipup
        del self.o_fake_reader

    def test_should_return_a_list_with_packages_when_called(self):
        packages = self.o_pipup.read_outdated_packages()

        self.assertGreater(
            len(packages), 0, "Package list should not be empty!")

    def test_should_return_an_empty_list(self):
        self.o_fake_reader.return_empty_list()
        packages = self.o_pipup.read_outdated_packages()

        self.assertListEqual(packages, [], "Package list should be empty!")
