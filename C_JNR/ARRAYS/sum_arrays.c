#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <conio.h>

int main(void)
{
    // int first_array[5];
    // int second_array[5];
    // int third_array[5];

    // printf("Enter first array:");
    // for (int i=0; i<5; i++)
    // {
    //     scanf("%d",&first_array[i]);
    // }
    // printf("Enter second array:");
    // for (int i=0; i<5; i++)
    // {
    //     scanf("%d",&second_array[i]);
    // }
    // for (int i=0; i<5; i++)
    // {
    //     int sum = first_array[i]+second_array[i];
    //     third_array[i]=sum;
    // }
    
    // for (int j=0; j<5; j++)
    // {
    //     printf("%d ",third_array[j]);
    // }

    char first_array[100];
    char second_array[100];
    int first_int[100];
    int second_int[100];
    int third_array[100];
    int index=0,index_2=0,index_3=0;
    
    printf("Enter first array:");
    fgets(first_array,sizeof(first_array),stdin);
    printf("Enter second array:");
    fgets(second_array,sizeof(second_array),stdin);

    char *token = strtok(first_array," ");

    while (token!=NULL)
    {
        int value_1 = atoi(token);
        first_int[index]=value_1;
        index++;
        token=strtok(NULL," ");
    }
    
    token=strtok(second_array," ");
    while (token!=NULL)
    {
        int value_2 = atoi(token);
        second_int[index_2]=value_2;
        index_2++;
        token=strtok(NULL," "); 
    }
    
    for (int i=0; i<index; i++)
    {
        int sum=first_int[i]+second_int[i];
        third_array[index_3]=sum;
        index_3++;
    }

    for (int i=0; i<index_3; i++)
    {
        printf("%d ",third_array[i]);
    }

    
    getch();
}

