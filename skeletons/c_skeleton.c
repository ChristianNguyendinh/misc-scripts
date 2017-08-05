/*
gcc c_skeleton.c -o <executable_name>
./<executable_name>

(or whatever other c compiler)
*/

#include <stdio.h>

void hello(char str[]) {
	printf("%s\n", str);
}

int main(void) {
	int i = 55;
	i += 10;

	printf("i is %d\n", i);

	hello("asdf");

	return 0;
}