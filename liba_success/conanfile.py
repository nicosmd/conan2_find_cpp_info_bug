from conan import ConanFile
from conan.tools.gnu import PkgConfig
from conan.tools import CppInfo

class BasicConanfile(ConanFile):
    name = "liba"
    version = "1.0.0"
    description = "A basic recipe"
    exports_sources = "liba.pc"


    def generate(self):
        pass

    def build(self):
        pass

    def package(self):
        pkg_config = PkgConfig(self, "liba", pkg_config_path=self.source_folder)
        cpp_info = CppInfo(self)
        pkg_config.fill_cpp_info(cpp_info, is_system=False)
        if len(cpp_info.libdirs) == 0:
            self.output.error("Lib dir path is empty but is should be /usr/lib")
        else:
            self.output.info("lib dir path is right!")
