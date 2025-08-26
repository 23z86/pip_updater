# pylint: disable=missing-docstring

from library.interfaces.updater_interface import UpdaterInterface


class DummyUpdater(UpdaterInterface):
    def run(self, **kwargs):
        pass
