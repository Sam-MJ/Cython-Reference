cdef extern from "include/hello_dll.h":
    int hello(char* name);
    int goodbye(char* name);
    int number();
