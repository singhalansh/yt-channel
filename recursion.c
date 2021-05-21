#include<stdio.h>
int a=0;
int func1(){
    printf("hello my name is Ansh.\n");
    if (a<11){
    a++;
    func1();
    }

}
int main()
{
    func1();


return 0;
}
