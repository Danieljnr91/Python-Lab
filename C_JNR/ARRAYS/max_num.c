#include <stdio.h>

int main(void)
{
    int numbers[10];
    printf("Enter numbers seperated by space\n:");
    for (int i=0; i<10; i++)
    {
        scanf("%d",&numbers[i]);
    }
    int highest=numbers[0];
    for (int j=0; j<10; j++)
    {
        if (numbers[j]>highest)
        highest=numbers[j];
    }
    printf("Highest = %d",highest);
    return 0;
}
