from library.interfaces.subprocess_interface import SubprocessInterface
from library.classes.read_subprocess import ReadSubprocess
from library.classes.update_subprocess import UpdateSubprocess


class SubprocessFactory:
    def get_subprocess(self, subprocess_type) -> SubprocessInterface:
        valid_subprocesses = {
            "read": ReadSubprocess(), "update": UpdateSubprocess()}

        return valid_subprocesses[subprocess_type]
