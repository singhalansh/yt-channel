#include<stdio.h>
int main()
{
    int a=1,n;
    printf("Enter the value of n\n");
    scanf("%d",&n);
    while(a<=n){
        printf("the value is: %d \n",a);
        // a++ ---> a+=1 or a= a+1
        a++;

    }
    return 0;
}