# include <stdio.h>

// int main(void)
// {
//     int x,y;
//     x = 10;
//     for (int i=0; i<=x; i++)
//     {
//         y = i + 2;
//         printf("%d\n",y);
//         printf("%d\n",i);
//     }
     
//     return 0;

// }


int main(void)
{
    int number , limit , answer;
    printf("Enter the number in which you want to generate the table for\n:");
    scanf("%d",&number);
    printf("Enter The limit of generation\n:");
    scanf("%d",&limit);
  

    for (int i=1; i>=1 && i <= limit; i++)
    {
        answer = i * number;
        printf("%d x %d = %d\n",number , i , answer);
    }


    return 0;
}