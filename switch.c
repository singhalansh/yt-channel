#include<stdio.h>
int main()
{
    int a;
    printf("enter the time according to following --> 1 -- 4am to 12 noon    2-- 12 noon to                 3-- 6pm to 10 pm                      4-- 10PM TO 4AM \n");
    scanf("%d",&a);

    switch(a)
    {
        case 1:
        printf("good morning");
        break;
        case 2:
        printf("good afternoon");
        break;
        case 3:
        printf("good evening");
        break;
        case 4:
        printf("good night");
        break;

    }
    return 0;
}