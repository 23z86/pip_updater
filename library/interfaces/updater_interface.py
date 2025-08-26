# pylint: disable=missing-docstring


from abc import ABC, abstractmethod


class UpdaterInterface(ABC):
    @abstractmethod
    def run(self, **kwargs):
        raise NotImplementedError
