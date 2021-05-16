#include<stdio.h>
int main()
{
    int a,n=1;
    printf("enter the number : \n");
    scanf("%d",&a);
    while (n<11)
    {
        /* code */
    printf("%d * %d = %d \n",a,n,a*n);
    n++;
    }
    
    return 0;
}