# include <stdio.h>
# include <conio.h>
int main(void)
{
   int first_num,second_num,answer;
   printf("Enter first number:");
   scanf("%d",&first_num);
   printf("Enter Second number");
   scanf("%d",&second_num);
   answer=first_num+second_num;
   printf("%d+%d=%d",first_num,second_num,answer);
   getch();
   return 0;


}
