''' topic - LOOPS in Python
there are two types of loops.
i.e. while loop and for loop

Definition:-the loops are peice of code that are
used to make same actions many times.

to get the multiplication table of any number'''
'''
#while loop syntax---
#i = 1
#while(i<21):
    #code
    #i+=1
num = int(input("enter the number please"))
i = 1
while(i<=10):
    print(num,"*",i,"=",num*i)
    i+=1 #i=i+1'''

'''#for loop syntax----->
#for i in range(start,end,step):
    #code
num = int(input("enter the number please"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)'''
    
'''lst = ["ansh","ayush","manish","kush","abhishek","shivani"]
for i in lst:
    print(i[1],end=" and ")
    #print(i)'''
'''i=0
while i<11:
    print("ansh",end=str(i))
    i+=2
    '''
'''
i= 1

while(i<12):
    j = 2
    while(j<12):
        print("hello there")
        j+=1
    i+=1'''

'''lst = []
a= "hello there"
for i in range(0,10):
    for j in range(1,11):
        print(a)
        lst.append(a)
        

print(len(lst))    '''

'''
   *
  ***
 *****
  ***
   *

   '''
'''for i in range(1,5):
    for j in range(4,i,-1):
        print(" ",end="")
    for k in range(1,i):
        print("*",end="")
    for l in range(2,i):
        print("*",end="")
    print()


    
for i in range(5,1,-1):
    for j in range(6,i,-1):
        print(" ",end="")
    for k in range(3,i):
        print("*",end="")
    for l in range(4,i):
        print("*",end="")
    print()'''


