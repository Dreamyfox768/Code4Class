#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
char *getDateAndTime();
int getInteger();
void decimalToBinary(int decValue, char binString[]);
void decimalToHex(int decValue, char hexString[]);
void decimalToOct(int decValue, char octString[]);
int saveFile(char name[], char date[], int decValue, char
octString[], char hexString[], char binString[]);
int main() {
char dateTime[32];
char name[32];
char binString[32];
char octString[32];
char hexString[32];
int decVal = 0;
int saveSuccess = 0;
strcpy(dateTime, getDateAndTime());
printf("Enter your name: ");
fgets(name, sizeof(name), stdin);
decVal = getInteger();
if (decVal == -1) {
printf("Goodbye!\n");
return 0;
}
decimalToBinary(decVal, binString);
decimalToHex(decVal, hexString);
decimalToOct(decVal, octString);
printf("Decimal: %d\n", decVal);
printf("Binary: %s\n", binString);
printf("Octal: %s\n", octString);
printf("Hexidecimal: %s\n", hexString);
saveSuccess = saveFile(name, dateTime, decVal, octString,
hexString, binString);
if (!saveSuccess)
return 1;
return 0;
}
char *getDateAndTime() {
time_t t;
time(&t);
return ctime(&t);
}
 loop
*/
int getInteger() {
char buffer[32];
int val;
printf("Enter an integer between 11000000 or type x to exit:
");
fgets(buffer, sizeof(buffer), stdin);
}
return -1;
}

void decimalToBinary(int decValue, char binString[]) {
int remainder, i = 0;
char binarynumber[100];
while (decValue != 0) {
remainder = decValue % 2;
decValue = decValue / 2;
binarynumber[i++] = remainder + '0';
}
for (int j = 0; j < i; j++) {
binString[j] = binarynumber[i - j - 1];
}
binString[i] = '\0';
}

void decimalToHex(int decValue, char hexString[]) {
int quotient = decValue;
int i = 0, temp;
char Hexaldecimal[100];
while (quotient != 0) {
temp = quotient % 16;
if (temp < 10)
temp = temp + 48;
else
temp = temp + 55;
Hexaldecimal[i++] = temp;
quotient = quotient / 16;
}
for (int j = 0; j < i; j++) {
hexString[j] = Hexaldecimal[i - j - 1];
}
hexString[i] = '\0';
}

void decimalToOct(int decValue, char octString[]) {
int quotient = decValue;
int i = 0, temp;
char octal[100];
while (quotient != 0) {
temp = quotient % 8;
temp = temp + 48;
octal[i++] = temp;
quotient = quotient / 8;
}
for (int j = 0; j < i; j++) {
octString[j] = octal[i - j - 1];
}
octString[i] = '\0';
}

int saveFile(char name[], char date[], int decValue, char
octString[], char hexString[], char binString[]) {
char user_input[10];
char filename[64];
FILE *filePtr;
printf("Save to a file? (y/n): ");
fgets(user_input, sizeof(user_input), stdin);
while (user_input[0] != 'y' && user_input[0] != 'n') {
printf("Error: illegal value\n");
printf("Save to a file? (y/n): ");
fgets(user_input, sizeof(user_input), stdin);
}
if (user_input[0] == 'n') {
return 1;
}
printf("Enter a file name: ");
fgets(filename, sizeof(filename), stdin);
filename[strcspn(filename, "\n")] = '\0';
filePtr = fopen(filename, "w");
if (filePtr == NULL) {
printf("Error opening file: %s\n", filename);
return 0;
}
fprintf(filePtr, "Name: %s", name);
fprintf(filePtr, "Date: %s", date);
fprintf(filePtr, "Decimal: %d\n", decValue);
fprintf(filePtr, "Binary: %s\n", binString);
fprintf(filePtr, "Octal: %s\n", octString);
fprintf(filePtr, "Hexadecimal: %s\n", hexString);
fclose(filePtr);
printf("File is saved\n");
return 1;
}
