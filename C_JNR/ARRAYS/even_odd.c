# include <stdio.h>

int main(void)
{
    int numbers[10];
    int even_num[10];
    int odd_num[10];
    int even_index = 0;
    int odd_index = 0;

    printf("Enter array of numbers:");
    for (int i=0; i<10; i++)
    {
        scanf("%d",&numbers[i]);
    }
    for (int sort=0; sort<10; sort++)
    {
        if (numbers[sort] % 2 == 0)
        {
           even_num[even_index] = numbers[sort];
           even_index += 1;
        }
        else
        {
            odd_num[odd_index] = numbers[sort];
            odd_index += 1;
        }
    }
    printf("Even number:");
    for (int even=0; even<even_index; even++)
    {
        printf("%d ",even_num[even]);
    }
    printf("\nodd numbers:");
      for (int odd=0; odd<odd_index; odd++)
    {
        printf("%d ",odd_num[odd]);
    }
    return 0;

}
