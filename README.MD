# Simple Reference for Dynamically linking a C library DLL to Python using Cython.

## .PXD
These are like header files and contain Cython declarations
A .pxd file is imported into a .pyx module by using the cimport keyword.
They cannot have the same name as the pyx files.

## .PYX
These are where you create the function wrappers.
- cdef or @cython.cfunc declare C functions only available within cython code.
- cpdef or @cython.ccall declares mixed functions that can call your declared C functions from Python.

## Building
setup.py and Makefile are our build system

include folder should contain C header files
libs folder should contain the .dll and .lib of your C libraries

## Running
Move the dll into the same dirctory as your python code
If you are on windows you can use os.add_dll_directory()

Import the pyd file into your python program and interact with it as normal

## Common errors
### AttributeError: module 'libname' has no attribute 'function_name'
This means the function you are trying to call is not visible to Python.
Check:
- It has been declared properly in .pxd
- Between the .pyx and .pxd it has cpdef/cython.ccall status so python can access it.
### ImportError: DLL load failed while importing libname: %1 is not a valid Win32 application.
- Check you are exporting the symbols you need for your dll in your C headers
PC: '\_\_declspec(dllexport)'
Unix: '\_\_attribute\_\_((visibility("default")))'

### LINK : fatal error LNK1181: cannot open input file 'filename'
The linker can't find a file it needs, such as .dll, .lib or .h.
Check the includes_dir and libs_dir in setup.py



## Mac - make sure it's the same python version building as running app

### lib is created called with -lib prefix, i.e. libhello, if you rename the linker cant find it. 

## library not loaded, image not found
rpath needs to be set at linker stage or at runtime - pass commands to cython
https://stackoverflow.com/questions/856116/changing-ld-library-path-at-runtime-for-ctypes
https://stackoverflow.com/questions/43551483/how-to-set-rpath-in-cmake
