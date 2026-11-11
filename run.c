#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int choose;

    printf("I am feeling lucky STL by zllai26.\n");
    printf("You can either select:\n");
    printf("1. Check how many STLs are there inside stls directory\n");
    printf("2. Let the computer choose a mesh for you\n");
    printf("> ");

    if (scanf("%d", &choose) != 1) {
        printf("Please enter a number.\n");
        return 1;
    }

    if (choose == 1) {
        system("venv/bin/python3 load.py");
    } else if (choose == 2) {
        system("venv/bin/python3 mesh.py");
    } else {
        printf("Invalid choice: %d\n", choose);
        return 1;
    }

    printf("\nPress Enter to exit...");
    getchar();
    getchar(); 

    return 0;
}