#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 1000

void shift_up(char buff[], int shift);
void shift_down(char buff[], int shift);

/*
TODO:
write output to file
take in command line arguments
comment
remove dSYM folder
*/

int main(void) {
	FILE *fp;
	char buff[BUFFER_SIZE];

	fp = fopen("test.txt", "r");

	while (fgets(buff, BUFFER_SIZE, fp) != NULL) {
		/*shift_up(buff, 10);*/
		shift_down(buff, 10);
		printf("%s", buff);

	}

	fclose(fp);

	return 0;
}

void shift_up(char buff[], int shift) {
	int ascii, i;
	for (i = 0; i < strlen(buff); i++) {
		ascii = (int) buff[i];

		if (ascii != 10 && ascii != 32 && ascii != 46) {
			if (ascii + shift > 126)
				buff[i] = 33 + (ascii + shift - 126);
			else
				buff[i] += shift;
		}
	}
}

void shift_down(char buff[], int shift) {
	int ascii, i;
	for (i = 0; i < strlen(buff); i++) {
		ascii = (int) buff[i];

		if (ascii != 10 && ascii != 32 && ascii != 46) {
			if (ascii - shift < 33)
				buff[i] = 126 - (33 - ascii - shift);
			else
				buff[i] -= shift;
		}
	}
}


