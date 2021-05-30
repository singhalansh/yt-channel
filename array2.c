#include<stdio.h>
int main()
{
    // int array1[7];
    // for(int i = 0; i<7; i++){
    //     printf("enter the value of %d element of array:\n",i);
    //     scanf("%d",&array1[i]);
    // }
    // for(int i = 0; i<7; i++){

    //     printf("the %d element of array is %d\n",i,array1[i]);
    // }
    int a[4][3];
    for(int i=0;i<4;i++){
        for(int j=0; j<3;j++){
            printf("enter the value of %d %d element of array:\n",i,j);

            scanf("%d",&a[i][j]);
        }
    }
    for(int i = 0; i<4;i++){
        for(int j=0; j<3;j++){
            printf("the %d %d element of array is %d\n",i,j,a[i][j]);
        }
    }

return 0;
}
