/*

Caesar Cipher using C.

Usage: 
gcc c_caesar.c -o c_caesar.x

To Shift Up by 1:
	./c_caesar.x test.txt -u 1
To Shift Down by 1:
	./c_caesar.x test.txt -d 1

Takes in three arguments: file name, -d or -u, and key to shift by.
Reads from file name, then shifts up or down based on -d or -u by key.
Writes shifted/unshifted output to a new file, with a name depending 
on whether it was shifted or un-shifted.

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 1000

void shift_up(char buff[], int shift);
void shift_down(char buff[], int shift);

int main(int argc, char **argv) {
	/* fp will is the file we are reading from and wp is the file we will write to*/
	FILE *fp, *wp;
	char buff[BUFFER_SIZE];
	char *path, *write_path;
	int shift;

	if (argc != 4) {
		perror("Was expecting 3 arguments. First being file path, second being -u or -d for shift up or down, and third the key to shift by");
		exit(2);
	}

	if (strcmp(argv[2], "-u") != 0 && strcmp(argv[2], "-d") != 0) {
		perror("Bad flag, was expecting either -u or -d for second argument");
		exit(2);
	}

	/* Get path and shift key from command line arguments */
	path = argv[1];
	shift = atoi(argv[3]);

	/* Open the file for reading */
	fp = fopen(path, "r");
	if (fp == NULL) {
		printf("Problem opening %s, exiting.", path);
		exit(1);
	}

	/* create the file name. 7 is length of Ushift_<filename> or Dshift_<filename> */
	write_path = malloc((strlen(path) + 7 + 1));
	if (write_path == NULL) {
		perror("Issue dynamically allocating data. Exiting");
		exit(2);
	}
	/* Get filename prefix to be appended with the given filename */
	if (strcmp(argv[2], "-u") == 0)
		strcpy(write_path, "Ushift_");
	else 
		strcpy(write_path, "Dshift_");

	strcat(write_path, path);
	/* Open the file for writing */
	wp = fopen(write_path, "w");
	if (wp == NULL) {
		printf("Problem creating %s to write to, exiting.", write_path);
		exit(1);
	}

	/* Read in each line, shift up or down, then write the result to the write file */
	while (fgets(buff, BUFFER_SIZE, fp) != NULL) {
		if (strcmp(argv[2], "-u") == 0)
			shift_up(buff, shift);
		else
			shift_down(buff, shift);

		/* Shift up or down will modify the buffer. Write to file.*/
		/* printf("%s", buff); */
		fputs(buff, wp);

	}

	fclose(fp);
	fclose(wp);

	printf("File successfully shift and written to: %s\n", write_path);

	return 0;
}

/* Shift characters in buffer up by shift key, wraps around to maintain ascii character */
void shift_up(char buff[], int shift) {
	int ascii, i;
	for (i = 0; i < strlen(buff); i++) {
		ascii = (int) buff[i];
		/* Skip spaces, newline, and periods */
		if (ascii != 10 && ascii != 32 && ascii != 46) {
			/* Wrap to beginning to maintain visible ascii characters */
			if (ascii + shift > 126)
				buff[i] = 33 + (ascii + shift - 126);
			else
				buff[i] += shift;
		}
	}
}

/* Shift characters in buffer down by shift key, wraps around to maintain ascii character */
void shift_down(char buff[], int shift) {
	int ascii, i;
	for (i = 0; i < strlen(buff); i++) {
		ascii = (int) buff[i];
		/* Skip spaces, newline, and periods */
		if (ascii != 10 && ascii != 32 && ascii != 46) {
			/* Wrap to maintain visible ascii characters */
			if (ascii - shift < 33)
				buff[i] = 126 - (33 - ascii - shift);
			else
				buff[i] -= shift;
		}
	}
}


