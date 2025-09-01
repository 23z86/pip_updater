# pylint: disable=missing-docstring


from abc import ABC, abstractmethod


class LoggerInterface(ABC):
    @abstractmethod
    def log(self):
        raise NotImplementedError
