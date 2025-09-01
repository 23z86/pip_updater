from library.classes.read_subprocess import ReadSubprocess
import unittest
from mocks.fake_subprocess import FakeReadSubprocess


class SubprocessRunnerSmokeTest(unittest.TestCase):
    def setUp(self):
        self.fake_subprocess = FakeReadSubprocess()
        self.subprocess_runner = ReadSubprocess(self.fake_subprocess)

    def test_run_returns_list(self):
        packages = self.subprocess_runner.run()
        self.assertEqual(packages[0]["name"], "FakeFlask")
