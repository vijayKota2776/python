#WAP to find the number of words in the given text file
file=open("./file_try.txt","w")
file.write("Happy Programming")
file.close()

file=open("./file_try.txt","r")
data=file.read()
print(data)
file.close()

file=open("./file_try.txt","r")
data1=file.readline()
print(data1)
file.close()

file=open("./file_try.txt","r")
data1=file.read(4)
print(data1)
file.close()

file=open("./file_try.txt","r")
data1=file.readlines()
for i in data1:
    print(i)
print("Data in list:",data1)
file.close()

file=open("./file_try.txt","a")
file.writelines("\n This is my second line iam including ")
file.close()

file=open("./file_try.txt","r")
data=file.read()
print(data)
file.close()