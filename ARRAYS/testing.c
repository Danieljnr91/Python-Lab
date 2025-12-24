#include <stdio.h>

// int main(void)
// {
//     int arr[7] = {6,7,4,8,6,7,1};
//     int highest = arr[0];
//     for (int i=0; i<7; i++)
//     {
//        if (arr[i] > highest)
//        {
//         highest=arr[i];
//     }
//     }
//     printf("The highest = %d",highest);
//     return 0;
// }



// ARRAY INPUT
int main(void)
{
    int arr[6];
    printf("Enter numbers seperated by space:");
    for (int i=0; i<6; i++)
    {
        scanf("%d",&arr[i]);
        printf("%d ",arr[i]);
    }
    return 0;
}
