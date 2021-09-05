from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration


class LibmatroskaConan(ConanFile):
    name = "libmatroska"
    version = "1.6.3"
    license = "LGPL-2.1"
    author = "David Bourgault contact@davidbourgault.ca"
    url = "https://github.com/ngc7293/libmatroska-conan"
    description = "a C++ libary to parse Matroska files (.mkv and .mka) "
    requires = ['libebml/1.4.2']
    topics = ("matroska", "multimedia", "av")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"

    def config_options(self):
        if self.settings.compiler == 'gcc' and self.settings.compiler.libcxx == 'libstdc++':
            raise ConanInvalidConfiguration('This library requires GCC C++11 ABI')

        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        self.run("git clone https://github.com/Matroska-Org/libmatroska.git --branch release-1.6.3 --depth=1")
        tools.replace_in_file("libmatroska/CMakeLists.txt", "project(matroska VERSION 1.6.3)",
                              '''project(matroska VERSION 1.6.3)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions['DISABLE_PKGCONFIG'] = 'Yes'
        cmake.configure(source_folder="libmatroska")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["libmatroska.a"] if not self.options.shared else ['libmatroska.so']
