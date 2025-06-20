#include "hello_dll.h"
#include <stdio.h>

int number(void) {
	return 42;
}

int hello(char* name) {
	printf("Hello %s\n", name);
	return 0;
}

int goodbye(char* name) {
	printf("Goodbye %s\n", name);
	return 0;
}
