#include <stdio.h>

int main(void)
{
    int first_num , last_num , choice , total=0;
    printf("Enter a range of numbers seperated by space\n:");
    scanf("%d %d",&first_num,&last_num);
    printf(
    "Do you wish to...\n"
    "1. Sum the numbers in given range\n"
    "2. Output only odd numbers\n"
    "3. Output only even numbers\n"
    "4. Count numbers in range\n"
    "Enter: "
);

    scanf("%d",&choice);
    if (choice==1)
    {
        for (int i=first_num; i<=last_num; i++)
        total += i;
        printf("The sum of numbers between %d and %d = %d",first_num,last_num,total);
    }
    else if (choice==2)
    {
        for (int i=first_num; i<=last_num; i++)
        if (i%2!=0)
        {
            printf("%d\n",i);
        }
    }
    else if (choice==3)
    {
        for (int i=first_num; i<=last_num; i++)
        if (i%2==0)
        {
            printf("%d\n",i);
        }
    }
    else
    {
        for (int i=first_num; i<=last_num; i++)
        total+=1;
        printf("There are (%d) digits between range of %d and %d",total,first_num,last_num);
    }
    return 0;
}