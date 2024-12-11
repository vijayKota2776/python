#program to remove duplicates from a list.
inpu=(input("Enter the numbers to remove the duplucates")).split(" ")
inpu=set(inpu)
print((inpu))

#function that takes two lists and returns True if they have at least one common member.
inpu1=(input("Enter the numbers or string ")).split(" ")
inpu2=(input("Enter the second numbers or string")).split(" ")
for i in inpu1:
    if i in inpu2:
        print(True)
        break
else:
    print(False)

    #program to print the numbers of a specified list after removing even numbers from it.
inpu=input("Enter the numbers to remove the duplucates").split(" ")
inpu=[int(i) for i in inpu]
inpu=[j for j in inpu if j%2!=0]
print(inpu)

#program to find the second smallest number in a list.
inpu=input("Enter the number to temm second smallest value").split(" ")
inpu=[int(i) for i in inpu]
# f=min(inpu)
inpu.remove(min(inpu))
print(f"The second smalles value is {min(inpu)} ")

#program to split a list every Nth element.
def split_list(input_list, n):
    return [input_list[i:i+n] for i in range(0, len(input_list), n)]
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3
print("Original List:", input_list)
print("Split List:", split_list(input_list, n))

#function to find the union and intersection of two lists
input_list = [1, 2, 3, 4, ]
input_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
input_list=set(input_list)
input_list2=set(input_list2)
print(f"union of the list {input_list ,input_list2} is \n{input_list.union(input_list2)}")
print(f"intersection of the sets 'a-b' is {input_list.intersection(input_list2)}")

#function to check if a list is a palindrome or not
inpu=input("Enter the number to cgheck the list is palandrem").split(" ")
inpu=[int(i) for i in inpu]
if inpu[::1]==inpu[::-1]:
    print(True)
else:
    print(False)