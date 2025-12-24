# include <stdio.h>

int main(void)
{   
    int number;
    printf("How many star patterns?:");
    scanf("%d",&number);
    for (int j=1; j<=20; j++)
    {
        for (int i=1; i<=number; i++)
        {    
        printf("*");
        }
        printf("\n");
    }


    return 0;
}