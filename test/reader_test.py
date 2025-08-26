import unittest

from library.classes.concrete_reader import ConcreteReader
from mocks.fake_subprocess_runner import SubprocessRunnerFake


class ReaderTest(unittest.TestCase):
    def setUp(self) -> None:
        self.o_subprocess_runner = SubprocessRunnerFake()
        self.o_reader = ConcreteReader(self.o_subprocess_runner)

    def tearDown(self) -> None:
        del self.o_reader
        del self.o_subprocess_runner

    def test_should_return_a_list_with_packages_when_called(self):
        packages = self.o_reader.run()

        self.assertGreater(
            len(packages), 0, "Package list should not be empty!")

    def test_should_return_an_empty_list(self):
        self.o_subprocess_runner.return_empty_list()
        packages = self.o_reader.run()

        self.assertListEqual(packages, [], "Package list should be empty!")
