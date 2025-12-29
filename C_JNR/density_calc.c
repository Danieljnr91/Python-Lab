#include <stdio.h>
#include <conio.h>
#include <math.h>
int main(void)
{
    double mass , volume , density;
    printf("Enter the mass(g) and volume in (cm^3):");
    scanf("%lf %lf",&mass,&volume);
    if (volume==0)
    {
        printf("ERROR! Volume cannot be equal to zero");
    }
    else
    {
        density=mass/volume;
        density=round(density*100)/100;
        printf("The density = %.2fg/cm^3\n",density);
    
   
        if (density<1) 
        {
           printf("An object with density of %.2fg/cm^3 will float on water",density);
        }
        else 
        {
        printf("An object with density of %.2fg/cm^3 will sink in water",density);
        }
    }
    getch();
    return 0;

}