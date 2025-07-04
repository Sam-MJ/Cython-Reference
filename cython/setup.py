from setuptools import setup, Extension
from Cython.Build import cythonize
from pathlib import Path
import platform

OUTPUT_NAME = "hellolib"
CYTHON_FILE = "hello.pyx"
C_LIBRARY_NAME = "hello_dll"

libs_dir = Path("./libs")
include_dir = Path("./include")

if platform.system() == 'Darwin':
    set_rpath = ["-rpath", '@loader_path/libs']
else:
    set_rpath = None

ext_modules = Extension(
    OUTPUT_NAME,
    [CYTHON_FILE],
    libraries=[C_LIBRARY_NAME],
    library_dirs=[libs_dir.as_posix()],
    include_dirs=[include_dir.as_posix()],
    extra_link_args=set_rpath
)

setup(
    name="Hello world app",
    ext_modules=cythonize(ext_modules),
)
