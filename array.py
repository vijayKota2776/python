# 1
def reverse(arr):
    return arr[::-1]
array = [1, 2, 3, 4, 5]
print(reverse(array))  

#2
def count(arr, element):
    return arr.count(element)
array = [1, 2, 3, 4, 3, 2, 1, 3]
element = 3
print(count(array, element)) 

#3
def duplicates(arr):
    return len(arr) != len(set(arr))
array = [1, 2, 3, 4, 5, 5]
print(duplicates(array))  

#4
def find(arr):
    total_sum = sum(range(min(arr), max(arr) + 1))
    return total_sum - sum(arr)
array = [1, 2, 3, 5]  
print(find(array))  

#5
def replace_odd(arr):
    return [-1 if x % 2 != 0 else x for x in arr]
array = [1, 2, 3, 4, 5]
print(replace_odd(array))  