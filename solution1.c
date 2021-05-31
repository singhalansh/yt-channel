#include<stdio.h>
int table(int num,int i){
    printf("%d * %d = %d\n",num,i,num*i);
    i++;
    if(i<11){
        table(num,i);
    }

}
int main()
{
    int num;
    printf("Enter the number please:\n");
    scanf("%d",&num);
    /* for loop*/
    // for(int i=1;i<11;i++){
    //     printf("%d * %d = %d\n",num,i,num*i);

    // }
    /*while loop*/
    // int i=1;
    // while(i<11){
    //     printf("%d * %d = %d\n",num,i,num*i);
    //     i++;
    // }
    // int i=1;
    // do{
    //     printf("%d * %d = %d\n",num,i,num*i);
    //     i++;
    // }while(i<=10);
    // int i=1;
    // table(num,i);


return 0;
}
