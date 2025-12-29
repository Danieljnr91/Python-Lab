# include <stdio.h>


int main(void)
{   printf("GEOMETRY CALCULATOR\n");
    printf("Choose Your Shape?\n");
    printf("1.Square\n");
    printf("2.Rectangle\n");
    printf("3.Triangle\n");
    printf("4.Circle\n");
    int shape_type;
    printf("Choose number which represents your shape:");
    scanf("%d",&shape_type);
    if (shape_type==1) {
        printf("Whats the length of shape");
        float length,area,perimeter;
        scanf("%f",&length);
        area = length * length;
        perimeter=4*length;
        printf("the area is %.2f cm^2\n",area);
        printf("The perimeter of your square is %.2fcm",perimeter);
    } else if (shape_type==4) {
      printf("Enter Radius:");
      float radius ,area,perimeter;
      scanf("%f",&radius);
      area = 3.145*radius*radius;
      perimeter=2*radius*3.145;
      printf("Area of cirlce is %.2fcm^2\n",area);
      printf("Circumference of circle is %.2fcm^2",perimeter);
    }
    
    


   
} 
