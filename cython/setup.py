from setuptools import setup, Extension
from Cython.Build import cythonize
from pathlib import Path

OUTPUT_NAME = "hellolib"
CYTHON_FILE = "hello.pyx"
C_LIBRARY_NAME = "hello_dll"

libs_dir = Path("./libs")
include_dir = Path("./include")

ext_modules = Extension(
    OUTPUT_NAME,
    [CYTHON_FILE],
    libraries=[C_LIBRARY_NAME],
    library_dirs=[libs_dir.as_posix()],
    include_dirs=[include_dir.as_posix()],
)

setup(
    name="Hello world app",
    ext_modules=cythonize(ext_modules),
)
