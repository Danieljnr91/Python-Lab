#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <conio.h>

int main(void)
{
    char scores[30];
    int score_array[30];    
    int index=0;
    double sum=0,average;
    printf("Enter scores seperated by space:");
    fgets(scores , sizeof(scores) , stdin);

    char *token = strtok(scores , " ");

    while (token!=NULL)
    {
        int values=atoi(token);
        score_array[index]=values;
        index++;
        token=strtok(NULL," ");
    }
    for (int i=0; i<index; i++)
    {
        sum += score_array[i];
        average=sum/index;
    }
    printf("Average score = %f",average);
    // for (int j=0; j<index; j++)
    // {
    //     printf("%d ",score_array[j]);
    // }
    // printf("\n index = %d",index);

    getch();
    return 0;
}