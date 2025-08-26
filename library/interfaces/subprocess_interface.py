# pylint: disable=missing-docstring


from abc import ABC, abstractmethod


class SubprocessInterface(ABC):
    @abstractmethod
    def run(self):
        raise NotImplementedError
