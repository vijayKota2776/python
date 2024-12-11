#element wise sum of the different tuple
in1=(1,2,3,4)
in2=(2,3,4,5)
in3=(3,4,5,6)
for i in range(len(in1)):
    s=in1[i]+in2[i]
    print(s+in3[i],end=" ")

# program to convert a given list of tuples to a list of lists. 
x=[(1, 2), (2, 3), (3, 4)]
x=[list(i) for i in x]
x

#program to remove an empty tuple(s) from a list of tuples.
x=[(1, 2), (2, 3), (3, 4),(),()]
x=[i for i in x if i]
print(x)

#program to convert a given string to a tuple
inpu=input("enter the string to conver it to tuple")
tupl=tuple(inpu)
print(tupl)

import math
#program to calculate the product, multiplying all the numbers in a given tuple.
inpu=(input("enter the numbers to numtiplay th numbers")).split(" ")
inpu=[int (i) for i in inpu ]
inpu=tuple(inpu)
print(math.prod(inpu))