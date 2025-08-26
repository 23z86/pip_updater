from library.interfaces.subprocess_interface import SubprocessInterface

class FakeSubprocess(SubprocessInterface):
    def run(self, *args, **kwargs):
        class Result:
            stdout = '[{"name": "FakeFlask", "version": "1.0", "latest_version": "1337"}]'
        return Result()
