# pylint: disable=missing-docstring


from abc import ABC, abstractmethod


class IUpdateStrategy(ABC):
    @abstractmethod
    def run(self, *args):
        raise NotImplementedError
