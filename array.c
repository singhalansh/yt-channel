#include<stdio.h>
int main()
{
    /* 
    (type) name[] = {elements};
    (type) name[size];

    (type) name[size][size] = {{first row},{second row}};
    (type) name[size][size];
    */
//    int arr[] = {1,2,3,4,5,6,7};
//    for(int i=0;i<7;i++){
//        printf("the %d element of array is: %d\n",i,arr[i]);
//    }
    int arr2[2][3]= { {1,2,3}, {4,5,6}} ;
    for(int i = 0; i<2;i++){
        for(int j=0; j<3;j++){
            printf("the %d %d element of array is %d\n",i,j,arr2[i][j]);
        }
    }


return 0;
}
