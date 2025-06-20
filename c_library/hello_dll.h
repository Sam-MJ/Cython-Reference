#pragma once
#ifndef HELLO_H
#define HELLO_H

__declspec(dllexport) int number(void);

__declspec(dllexport) int hello(char* name);

__declspec(dllexport) int goodbye(char* name);

#endif
