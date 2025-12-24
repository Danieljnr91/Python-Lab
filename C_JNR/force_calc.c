#include <stdio.h>
#include <math.h>

int main(void)
{
    printf("FORCE CLACULATOR\n");
    printf("What do you wish to find?\n1.Force \n2.Mass \n3.Acceleration\nEnter:");
    int operation;
    double force,mass,acceleration;
    scanf("%d",&operation);
    
    if (operation==1)
    {
        printf("Enter mass and acceleration seperated by space:");
        scanf("%lf %lf",&mass,&acceleration);
        if (mass<=0 || acceleration<0)
        {
            printf("ERROR! Invalid Input Detected");
        }
        else
        {
           force = mass * acceleration;
           force = round(force*100)/100;
           printf("The force = %.2lfN",force);
        }
        
    }
    else if (operation==2)
    {
        printf("Enter force and accleration seperated by space:");
        scanf("%lf %lf",&force,&acceleration);
        if (acceleration<=0)
        {   
            acceleration=(acceleration);
            printf("ERROR! Invalid Input Detected (%.lf)",acceleration);
        }
        else
        {
            mass=force/acceleration;
            mass = round(mass*100)/100;
            printf("The mass = %.2fkg",mass);
        }
    }
    else
    {
        printf("Enter force and mass seperated by space:");
        scanf("%lf %lf",&force,&mass);
        if (mass<=0)
        {
            mass = round(mass);
            printf("ERROR! Invalid Input Detected");
        }
        else
        {
            acceleration = force/mass;
            acceleration=round(acceleration*100)/100;
            printf("The acceleration = %.2fms^-2",acceleration);
        }
    }

    return 0;
}