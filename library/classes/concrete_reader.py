# pylint: disable=missing-docstring
from library.interfaces.reader_interface import ReaderInterface
from library.interfaces.subprocess_interface import SubprocessInterface

class ConcreteReader(ReaderInterface):
    def __init__(self, o_subprocess_runner: SubprocessInterface):
        self.o_subprocess_runner = o_subprocess_runner

    def run(self):
        pip_list = self.o_subprocess_runner.run()

        return pip_list
