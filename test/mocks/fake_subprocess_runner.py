from library.interfaces.subprocess_interface import SubprocessInterface


class SubprocessRunnerFake(SubprocessInterface):
    def __init__(self):
        self.test_for_empty_list = False

    def return_empty_list(self):
        self.test_for_empty_list = True

    def run(self):
        if self.test_for_empty_list:
            return []

        packages = [
            {
                "name": "FakeRequests",
                "version": "0.0",
                "latest_version": "1337"
            },
            {
                "name": "FakeFlask",
                "version": "1.0",
                "latest_version": "1337"
            }
        ]
        return packages
