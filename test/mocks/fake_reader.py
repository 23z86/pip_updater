from library.interfaces.reader_interface import ReaderInterface


class FakeReader(ReaderInterface):
    def run(self):
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
