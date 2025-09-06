# pylint: disable=missing-docstring

from abc import ABC, abstractmethod


class RequestsInterface(ABC):

    @abstractmethod
    def execute(self, **kwargs):
        raise NotImplementedError
