import numpy as np
#program to reverse the order of the items in the array.
lis=(input("enter the values into the array"))
data_list=lis.split()
array=np.array(data_list,dtype=int)
for i in range(len(array)//2):
    s=array[i]
    array[i],array[-(i+1)]=array[-(i+1)],s
print(array)
print(type(array))

# Python program to get the number of occurrences of a specified element in an array.
lis=(input("enter the values into the array"))
data_list=lis.split()
array=np.array(data_list,dtype=int)
dec={}
for i in range(len(array)):
    if array[i] in dec:
        dec[array[i]]+=1
    else:
        dec[array[i]]=1
print(dec)

#Python program to find out if a given array of integers contains any duplicate elements.
lis=(input("enter the values into the array"))
data_list=lis.split()
array=np.array(data_list,dtype=int)
s=set(array)
print(s)


#Python program to find the missing number in a given array of 5 continuous numbers.
array=np.array([1,2,3,4,None,6])
i=0
while i < len(array):
    if array[i]==None:
        array[i]=array[i-1]+1
    i+=1
print(array)

#Replace all odd numbers in the given array with -1
lis=(input("enter the values into the array"))
data_list=lis.split()
array=np.array(data_list,dtype=int)
for i in range(len(array)):
    if array[i]%2!=0:
        array[i]=(-1)
print(array)
