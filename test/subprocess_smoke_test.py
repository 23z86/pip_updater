from library.classes.subprocess_runner import SubprocessRunner
import unittest
from mocks.fake_subprocess import FakeSubprocess


class SubprocessRunnerSmokeTest(unittest.TestCase):
    def setUp(self):
        self.fake_subprocess = FakeSubprocess()
        self.subprocess_runner = SubprocessRunner(self.fake_subprocess)

    def test_run_returns_list(self):
        packages = self.subprocess_runner.run()
        self.assertEqual(packages[0]["name"], "FakeFlask")
