# pylint: disable=missing-docstring

from library.interfaces.subprocess_interface import SubprocessInterface

class FakeUpdateSubprocess(SubprocessInterface):
    def __init__(self):
        self.package_name = None
        self.old_version = "1.3.3.0"
        self.new_version = "1.3.3.7"
        
    def run(self, *args, **kwargs):
        package_name = args[0][-1]
        self._set_package_name(package_name)
    
    def _set_package_name(self, package_name):
        self.package_name = package_name
        
    def expect_version_differs(self):
        return self.old_version != self.new_version
    
    def expect_no_update_needed(self, version="1.3.3.7"):
        return self.new_version == version
    
    def expect_called_with_package(self, package_name):
        return package_name == self.package_name