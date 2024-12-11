'''''''''
#program to find the strig is palindrom and symmetrical
str=input("enter the string")
if str[::]==str[::-1]:
    print(f"The string you entred is palindrom :{str}")
else:
    print(f"The string is not palindrom ")
if len(str)%2==0:
    if str[:len(str)//2]==str[len(str)//2:]:
        print(f"The entered string is symmetrical :{str}")
    else:
        print(f"The string is not symmetrical ")
else:
    if str[:len(str)//2]==str[len(str)//2+1:]:
        print(f"The entered string is symmetrical :{str}")
    else:
        print(f"The string is not symmetrical ")

# length of string
str=input("enter the string for count")
count=0
for i in str:
    count+=1
print(f"the length of string is:{count}")

#To remove all the duplicates from the string
str=input("enter the string to remove all the duplicates")
se=set()
for i in str:
    se.add(i)
print(f"The string without duplicate is :{se}")

#Maximum frequency character in String
str=input("enter the string to know more repeated character ")
di={}
for i in str:
    if i in di:
        di[i]+=1
    else:
        di[i] =1
print(f"The more frequency value in this {str} is {max(di,key=di.get)} value is :{max(di.values())}")

#count the number of characters
str=input("enter the string to know the number of chracters with frequency ")
di={}
for i in str:
    if i in di:
        di[i]+=1
    else:
        di[i] =1
print(di)


#Count all letters, digits, and special symbols
str=input("enter the string with all the combinations")
l=["!","@","#",'$',"%","^","&","*","(",")","?","|","<",">","+","=","~",".",",","/","`"]
digit,specal,alpha=0,0,0
for i in str:
    if i.isdigit():
        digit+=1
    elif i in l[::1]:
        specal+=1
    else:
        alpha+=1
print(f"The number of digits are {digit} and num of specal symbol is {specal} alphabets are {alpha}")

#read incoming email
email=input("enter the mailid ")
spam=list()
if email.split("@")[1] =="itm.edu":
    print("This mail is with collage id \n sending it to pubic folder")
else:
    print("It is spam mail")
    spam.append(email)
 
'''
# #simple password validator
l=["!","@","#",'$',"%","^","&","*","(",")","?","|","<",">","+","=","~",".",",","/","`"]
capital,small,specal,num=False,False,False,False
pas=input("plese enter the pasword with these conditions \n 1.Atleast of 8 letters \n 2.One upper case \n 3.Atlest one specal symbol \n 4.One lower case \n \t")
T=True
while T!=False:
    if len(pas)<8:
        pass
    else:
        for i in pas:
            if ord(i)>=65 or ord(i)<=90:
                capital=True
            if ord(i)>=97 or ord(i)<=122:
                small=True
            if ord(i)>=0 or ord(i)<=9:
                num=True
            if i in l:
                specal=True
    if capital==True and small==True and num==True and specal==True:
        print(f"your password is correct \n The password you entered is {pas}")
        T=False
    else:
        pas=input("#####Incorrect password ##### \n Reenter the password \t")

