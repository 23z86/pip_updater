import logging

from library.interfaces.logger_interface import LoggerInterface


class InformationLogger(LoggerInterface):
    def __init__(self):
        logging.basicConfig(filename='.log', level=logging.INFO,
                            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    def log(self):
        return super().log()
