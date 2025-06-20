import cython
from cython.cimports import chello


@cython.ccall
def hello(name: str):
    byte_string = name.encode("utf-8")
    chello.hello(byte_string)


@cython.ccall
def goodbye(name: str):
    byte_string = name.encode("utf-8")
    chello.goodbye(byte_string)


@cython.ccall
def number():
    return chello.number()
