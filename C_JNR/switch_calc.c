# include <stdio.h>

int main(void)
{
    printf("CALCULATOR\n");
    double first_num , second_num , output;
    int operation;
    printf("Enter the numbers you want to operate on seperated by space:");
    scanf("%lf %lf",&first_num ,&second_num);
    printf("Choose Operation\n1.Addition \n2.Subtraction \n3.Dvision \n4.Multipliction \nEnter:");
    scanf("%d",&operation);
    switch (operation)
    {
        case 1:
            output=first_num+second_num;
            printf("%.2lf + %.2lf = %.2lf",first_num,second_num,output);
            break;
        case 2:
            output=first_num-second_num;
            printf("%.2lf - %.2lf = %.2lf",first_num,second_num,output);
            break;
        case 3:
            output=first_num/second_num;
            if (second_num==0)
            {
                printf("Division By 0 error!");
                break;
            }
            else
            {
                printf("%.2lf / %.2lf = %.2lf",first_num,second_num,output);
                break;
            }
        case 4:
            output=first_num*second_num;
            printf("%.2lf x %.2lf = %.2lf",first_num,second_num,output);
            break;
        default:
              printf("Error!");
    }
    return 0;
}