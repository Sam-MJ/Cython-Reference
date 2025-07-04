#pragma once
#ifndef HELLO_H
#define HELLO_H

#if   defined _WIN32
#define LIB_EXPORT __declspec(dllexport)
#else
#define LIB_EXPORT
#endif

LIB_EXPORT int number(void);
LIB_EXPORT int hello(char* name);
LIB_EXPORT int goodbye(char* name);

#endif
