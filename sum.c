#include<stdio.h>

int func1(){
    int a,b;
    printf("enter the value of a : \n");
    scanf("%d",&a);
    printf("enter the value of b: \n");
    scanf("%d",&b);
    return a+b;
}
int main()
{
    int c = func1();
    printf("the sum is: %d",c);


return 0;
}

