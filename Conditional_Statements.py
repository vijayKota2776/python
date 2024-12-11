
#1
year=int(input("enter the year "))
if(year%4==0):
    print("the year is leap year (year)")
else:
     print("the year is not leap year (year)")
     
#2
num=(input("enter the name which is having 3 digit "))
if len(num)==3:
    print("the number you entered is three digit ")
else:
    print("the number you entered is not three digit ")
    
#3
age=(input("enter the age"))
if ("age>=18"):
    print("you are eligible to vote ")
else:
    print("you are not eligible to vote ")
    
#4
num=(input ("enter a number"))
if(-1=="3"):
    print("the number you entered ends with 3")
else:
    print("the number you entered dose not end with 3")
    
#5
input_=(input("enter a character "))
if (input_=="a"or input_=="e"or input_=="i" or input_=="o" or input_=="u"or input_=="A" or input_=="E" or input_=="I" or input_=="O" or input_=="U"):
    print("the character is not a vowel ")
else:
    print("the character is consonant ")
    
#6
month=(input("enter the month name "))
if(month=="January " or month=="March" or month=="may" or month=="July" or month=="August" or month=="October"or month=="December"):
    print("this month have 31 days ")
elif month=="February ":
    print("this month have 28 days ")
else:
    print("this month have 30 days ")


#7
side1=int(input("Enter the first side of triangle: "))
side2=int(input("Enter the second side of triangle: "))
side3=int(input("Enter the third side of triangle: "))
if side1==side2==side3:
    print("The triangle is an Equilateral traingle")
elif side1!=side2 and side1!=side3 and side2!=side3:
    print("This is a Scalene traingle")
else:
    print("This is an Isoceles triangle")   
    
    
#8
electricity=int(input("enter the no of unit of electricity used:"))
if(electricity<=0):
    print("you will never get this uncle ")
elif(electricity<=100):
    print("congratulations government gave you free this time ")
elif(electricity>100 and electricity<200):
    print(f"sorry bro you will have to pay {(electricity-100)*5}")
else :
    print(f"bro you are expensive pay {(electricity-200)*10+500}")
    



#9
amount=int(input("enter the cose of your bike "))
if amount>=100000:
    print("the road tax of your favourite bike is '15%' ")
elif amount>=50000 and amount <=100000 :
    print("the road tax is '10%'")
else:
    print("the road tax is '5%'")

# 10
bill=int(input("enter the power bill"))
if (bill >10000):
    print(f"the bill is not having any charge {bill * 0.2} ")
elif bill>=7000 and bill<=10000:
    print(f"you used more units sorry you should pay the amount{bill * 0.15}")
else:
    print(f"you are rich pay the bill {bill * 0.1}")
    

