#include <stdio.h>

int main(void)
{
    char first_name[] = "James";
    char second_name[] = "Lebron";
    printf("Your full name is %s %s\n",first_name,second_name); 
    char fletter = 'A';
    char sletter = 'B';
    char tletter=130;
    unsigned char filetter = 156;
    printf("%c\n",fletter);
    printf("%d\n",sletter);
    printf("%d\n",tletter);
    printf("%c\n",tletter);
    printf("%d\n",filetter);
    printf("%c",filetter);
    return 0;
}