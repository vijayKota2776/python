# 1
num=int(input("enter a number"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
print(" ")

# 2
number = int(input("Enter a number: "))
digit_count = 0
while number != 0:
    number //= 10
   
    digit_count += 1
print(f"Total number of digits: {digit_count}")

# 3
lis=[1,2,3,4,5,6,7]
for i in lis:
    print(lis[-i],end=" ")

# 4
def print_prime_numbers(start, end):
    for num in range(start, end + 1):
        
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                print(num, end=" ")



# 5
def fibonacci_series(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1


# 6
num=int(input("enter the  umber to reverse"))
while num!=0:
    print(num%10,end="")
    num//=10

# 7
num=int(input("enter the number for sum of even and odd"))
even,odd=0,0
for i in range(num+1):
    if i%2==0:
        even+=i
    else:
        odd+=i
print(f"the sum of even numbers is {even} and the odd is {odd}")

# 8
def count_letters_digits(input_string):
    letters = digits = 0

    for char in input_string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1

    print(f"Letters {letters} Digits {digits}")



# 9a
num=int(input("enter the nuber for pattern"))
for i in range(num,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
# 9b
for i in range(1,6):
    for j in range(1,i+1):
        print("$",end=" ")
    print('')

for i in range(1,6):
    for j in range(1,5-i):
        print("*",end=" ")
    print('')

