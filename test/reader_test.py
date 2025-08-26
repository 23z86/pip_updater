import unittest

from mocks.fake_reader import FakeReader
from mocks.dummy_updater import DummyUpdater
from library.classes.pipup import PipUp

class ReaderTest(unittest.TestCase):
    def setUp(self) -> None:
        self.o_pipup = PipUp(FakeReader(), DummyUpdater())
    
    def tearDown(self) -> None:
        del self.o_pipup
        
    def test_should_return_a_list_with_packages_when_called(self):
        packages = self.o_pipup.read_outdated_packages()
        
        self.assertIsNotNone(packages, "Package list should not be empty!")