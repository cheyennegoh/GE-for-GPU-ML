/*****************************
 **
 **  mkspiral.c: A program
 **  to generate training
 **  data for a network with
 **  2 inputs and 1 output.
 **
 **  Any questions or comment
 **  on this task contact:
 **    Alexis P. Wieland
 **    MITRE Corporation
 **    (703) 883-7476
 **    wieland@mitre.ARPA
*****************************/

#include <stdio.h>
#include <math.h>

main()
{
    int i;
    double x, y, angle, radius;

    /* write spiral of data */
    for (i = 0; i <= 96; i++) {
        angle = i * M_PI / 16.0;
        radius = 6.5 * (104 - i) / 104.0;

        x = radius * sin(angle);
        y = radius * cos(angle);

        printf("%8.5f %8.5f %3.1f\n", x, y, 1.0);
        printf("%8.5f %8.5f %3.1f\n", -x, -y, 0.0);
    }
}