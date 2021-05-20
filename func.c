#include<stdio.h>
/* Basic syntax for declaring a function
(type) name(int a, int b){
    code;
}
*/
/*
calling A FUNCTION
name(a,b);
*/
int func1(){
    int a,b;
    printf("enter the value of a : \n");
    scanf("%d",&a);
    printf("enter the value of b: \n");
    scanf("%d",&b);
    printf("the value you entered are : %d %d",a,b);
}
int main()
{
    func1();


return 0;
}
