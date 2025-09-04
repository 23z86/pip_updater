# pylint: disable=missing-docstring

from library.interfaces.reader_interface import ReaderInterface
from library.classes.read_subprocess import ReadSubprocess


class ConcreteReader(ReaderInterface):
    def __init__(self):
        self.o_subprocess_runner = ReadSubprocess()

    def run(self):
        pip_list = self.o_subprocess_runner.run()

        return pip_list
