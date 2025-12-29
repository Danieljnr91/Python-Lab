#include <stdio.h>
#include <string.h>

int main(void)
{
    printf("INTRODUCTION\n");

    char first_name[20];
    char second_name[20];
    char school_name[30];

    printf("Enter Your First name:");
    fgets(first_name , 20 , stdin);
    first_name[strcspn(first_name,"\n")]='\0';

    printf("Enter Your second name:");
    fgets(second_name,20,stdin);
    second_name[strcspn(second_name, "\n")]='\0';

    printf("Enter The name of your school:");
    fgets(school_name,30,stdin);
    school_name[strcspn(school_name,"\n")]='\0';

    printf("My name is %s %s, i attended %s during my youth",first_name,second_name,school_name);
    return 0;

}
