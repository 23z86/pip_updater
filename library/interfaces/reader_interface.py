# pylint: disable=missing-docstring


from abc import ABC, abstractmethod


class ReaderInterface(ABC):
    @abstractmethod
    def run(self):
        raise NotImplementedError
