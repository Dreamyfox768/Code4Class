


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>

#define MAX_RECORDS 100

struct address_t {
    int address[20];char alias[20];  };
    struct address_t arrayaddress[100];  

int look_for_num = 0;
int size = 0;

char *getDateAndTime();  //  1- getime and date - the time
int readDataFile(const char *filename, char username[]);  // 2.  2- read data file -read file
void specifyLocality(int *local_1, int *local_2, int total);  // 3.  3- speify locality - prompt user fo rlocality pair, include range check
void generateLocalityReport(char username[], int local_1, int local_2, int report);  //  4- regereate locality report - this would be file output

int main(void) {
    char username[32];
    int local_1, local_2;
    int report;

    printf("\nEnter your name: ");
    fgets(username, sizeof(username), stdin);
    char *pos;
    if ((pos = strchr(username, '\n')) != NULL) // remove line from notes 
        *pos = '\0';

    report = readDataFile("CS222_Inet.txt", username);
    specifyLocality(&local_1, &local_2, report);
    generateLocalityReport(username, local_1, local_2, report);

for (int i = 0; i < size; i++) {
    if (arrayaddress[i].address[0] == local_1 &&
        arrayaddress[i].address[1] == local_2) {
        printf("%d.%d.%d.%d %s\n",
               arrayaddress[i].address[0], arrayaddress[i].address[1],
               arrayaddress[i].address[2], arrayaddress[i].address[3],
               arrayaddress[i].alias);
    }
}


    printf("\n GOOD Bye! ");
    return 0;
}

char *getDateAndTime() {
    time_t t;
    time(&t);
    return ctime(&t);
}

int readDataFile(const char *filename, char username[]) {
    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        printf("Error: cannot open file %s\n", filename); // if can't find file
        return 1;
}

    char line[64];
    while (fgets(line, sizeof(line), fp) != NULL && look_for_num < MAX_RECORDS) {
        int b[4];
        char name[20];

        if (sscanf(line, "%d.%d.%d.%d %s", &b[0], &b[1], &b[2], &b[3], name) == 5) {
            if (b[0] == 0 && b[1] == 0 && b[2] == 0 && b[3] == 0 && strcmp(name, "NONE") == 0) {
                break;
}

            for (int i = 0; i < 4; i++) {
                arrayaddress[look_for_num].address[i] = b[i];
}
            strcpy(arrayaddress[look_for_num].alias, name);

            look_for_num++;
}
}

    size = look_for_num;
    fclose(fp);
    return look_for_num;
}

void specifyLocality(int *local_1, int *local_2, int total) {
    int x = 0; 

    while (x < 20) { 
        printf("Enter locality value #1 [0–255]: ");
        if (scanf("%d", local_1) != 1 || *local_1 < 0 || *local_1 > 255) { // making sure number not outside of range for both locality
            printf("Error: %d is out of range. \n", *local_1);
            x++;
            continue;
}

        printf("Enter locality value #2 [0–255]: ");
        if (scanf("%d", local_2) != 1 || *local_2 < 0 || *local_2 > 255) {
            printf("Error: %d is out of range. \n", *local_2);
            x++;
            continue;
}

        // finding the first 2 localities 
        int i = 0;
        while (i < total &&
               !(arrayaddress[i].address[0] == *local_1 &&
                 arrayaddress[i].address[1] == *local_2)) {
            i++;
}

        if (i == total) {
            printf("Error: No records exist at location %d.%d\n", *local_1, *local_2);
            x++;
}       else {
            break;
}
}
}

// Week 5 for file  processing code: Generate locality report
void generateLocalityReport(char username[], int local_1, int local_2, int report) { // just fprint all information in the file and that is it 
    FILE *out = fopen("222_Locality_List.txt", "w");{
    char *datetime = getDateAndTime();
    fprintf(out, "%s\n%s\n", username, datetime);
    fprintf(out, "Records at %d.%d:\n", local_1, local_2);
    printf("\nRecords at %d.%d:\n", local_1, local_2);
    for (int i = 0; i < size; i++) { 
        if (arrayaddress[i].address[0] == local_1 &&
            arrayaddress[i].address[1] == local_2) {
            fprintf(out, "%d.%d.%d.%d %s\n",
                arrayaddress[i].address[0], arrayaddress[i].address[1],
                arrayaddress[i].address[2], arrayaddress[i].address[3],
                arrayaddress[i].alias);

        look_for_num++;
}
}

    fclose(out);
}
}

