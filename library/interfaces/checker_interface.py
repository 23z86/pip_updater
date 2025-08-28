# pylint: disable=missing-docstring


from abc import ABC, abstractmethod


class CheckerInterface(ABC):
    @abstractmethod
    def run(self, **kwargs):
        raise NotImplementedError
