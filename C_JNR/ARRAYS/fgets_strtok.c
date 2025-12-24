# include <stdio.h>
# include <string.h>
# include <stdlib.h>

// COUNT NUMBERS
// int main(void)
// {
//     char numbers[20];
//     int count=0;
//     printf("Enter numbers by space:");
//     fgets(numbers , sizeof(numbers) , stdin);

//     char *token = strtok(numbers," ");

//     while (token != NULL)
//     {
//         count ++;
//         token = strtok(NULL, " ");
//     }
//     printf("You Entered %d numbers",count);
//     return 0;
// }


// SUM NUMBERS
// int main(void)
// {
//     char numbers[50];
//     int sum=0;
//     printf("Enter the numbers you want to sum up\n:");
//     fgets(numbers, sizeof(numbers), stdin);
//     char *token = strtok(numbers," ");
//     while(token != NULL)
//     {
//         int value = atoi(token);
//         sum += value;
//         token = strtok(NULL , " ");
//     }
//     printf("The sum of the number is %d",sum);
//     return 0;
// }


// MAX AND MIN
// int main(void)
// {
//     char numbers[50];
//     printf("Enter numbers sepearated by space:");
//     fgets(numbers, sizeof(numbers), stdin);
    
//     char *token = strtok(numbers, " ");
//     int highest = atoi(token);
//     while (token != NULL)
//     {   
//         int values = atoi(token);
//         if (values > highest)
//         {
//             highest = values;
//         }
//         token = strtok(NULL , " ");
//     }
//     printf("The highest value = %d",highest);
// }


// EVEN ODD
int main(void)
{
    char numbers[50];
    int even_num[50];
    int odd_num[50];
    int even_index=0 , odd_index=0;
    printf("Enter array of numbers\n:");
    fgets(numbers, sizeof(numbers), stdin);

    char *token = strtok(numbers , " ");

    while (token != NULL)
    {
      int values = atoi(token);
      if (values % 2 == 0)
      {
         even_num[even_index] = values;
         even_index+=1;
      }
      else
      {
         odd_num[odd_index] = values;
         odd_index+=1;
      }
         token = strtok(NULL, " ");        
   }
   printf("Even numbers:");
   for (int i=0; i<even_index; i++)
   {
      printf("%d ",even_num[i]);
   }
   printf("\nOdd Numbers:");
   for (int j=0; j<odd_index; j++)
   {
      printf("%d ",odd_num[j]);
   }
   return 0;
}