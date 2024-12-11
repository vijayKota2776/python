#program to remove an item from a set if it is present in the set.
inp=input("enter the number to remove the numbers").split(" ")
re=int(input("which element you want remove"))
inp=[int (i) for i in inp]
inp=set(inp)
if re in inp:
    inp.remove(re)
else:
    print("The element is not there in set")
print(inp)

#program to check if two given sets have no elements in common
inp=input("enter the number for the first set").split(" ")
inp=[int (i) for i in inp]
inp=set(inp)
inp1=input("enter the number to second set").split(" ") 
inp1=[int (i) for i in inp1]
inp1=set(inp1)
print("The common elements the sets are ",(inp&inp1))

#program toGet Only unique items from two sets
inp=input("enter the number for the first set").split(" ")
inp=[int (i) for i in inp]
inp=set(inp)
inp1=input("enter the number to second set").split(" ") 
inp1=[int (i) for i in inp1]
inp1=set(inp1)
print("The common elements the sets are ",(inp-inp1))
print("The common elements the sets are ",(inp1-inp))

#program to Convert Set to one String
inp=input("enter the number for the first set").split(" ")
inp=set(inp)
string=""
for i in inp:
    string=string+i
print(string)

#program to count number of vowels using sets in given string
inp=input("enter the number for the first set")
s={"a","e","i","o","u","A","E","I","O","U"}
count=0
for i in inp:
    if i in s:
        count+=1
print(f"the numberts os ovels in string is {count}")