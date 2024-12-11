# 1. Write a Python class that has two methods: get_String and print_String , get_String
# accept a string from the user and print_String prints the string in upper case.

class strings:
    def get_string(self):
        self.user_input=input("Enter the string: ")
    def print_string(self):
        print(self.user_input.upper())

obj=strings()
obj.get_string()
obj.print_string()


# 2. Write a Python program to create a calculator class. Include methods for basic
# arithmetic operations.
class calc:
    def __init__(self):
        self.n1=int(input("Enter the first number: "))
        self.n2=int(input("Enter the second number: "))
    def addition(self):
        res1=self.n1+self.n2
        print('The addition is:',res1)
    def subtract(self):
        res2=self.n1-self.n2
        print('Subtraction is:',res2)
    def product(self):
        res3=self.n1*self.n2
        print('Product is:',res3)
    def divide(self):
        quo=self.n1//self.n2
        rem=self.n1%self.n2
        div=self.n1/self.n2
        print('Divison is:',div,'\nQuotient is:',quo,'\nRemainder is:',rem)
        
obj2=calc()
obj2.addition()
obj2.subtract()
obj2.product()
obj2.divide()


# 3. Write a Python class named Circle constructed from a radius and two methods that
# will compute the area and the perimeter of a circle.
class circle:
    pi=3.14
    def __init__(self):
        self.r=int(input("Enter the radius of circle: "))
    def area(self):
        area=(self.r**2)*self.pi
        print('Area of circle is:',area)    
    def circumference(self):
        circum=2*self.pi*self.r
        print("Circumference of circle is:",circum)
obj3=circle()
obj3.area()
obj3.circumference()


# 4. Write a Python class to implement pow(x, n).
class power:
    def __init__(self):
        self.x=int(input("Enter the Number: "))
        self.n=int(input("Enter the Power: "))
    def pow(self):
        result=self.x**self.n
        print(result)
obj4=power()
obj4.pow()


# 5. Write a Python program to create a class representing a shopping cart. Include
# methods for adding and removing items, and calculating the total price.
class Shopping:
    def __init__(self):
        self.shop_list={}
    def add_item(self):
        while True:
            item_input=input("Enter item and price (say 'end' to stop): ")
            if item_input.lower()=='end':
                break
            item,price=item_input.split()
            self.shop_list[item]=float(price)
    def remove_item(self):
        while True:
            remove_item=input("Enter item to remove (say 'no' to stop): ")
            if remove_item.lower()=='no':
                break
            self.shop_list.pop(remove_item, None)  #None used if user accidently put wrong spelling
    def add_total(self):
        total = sum(self.shop_list.values())
        print('Total cost:', total, 'Rupees')
obj=Shopping()
obj.add_item()
obj.remove_item()
obj.add_total()


# 6. Write a Python class Employee with attributes like emp_id, emp_name,
# emp_salary, and emp_department and methods like
# calculate_emp_salary, emp_assign_department, and print_employee_details. 
# (More data was there but did not write - question too big)
class Employee:
    def __init__(self, emp_id, name, salary, hours, department):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.overtime_hours = max(0, hours - 50)     #good trick to remember-soham 20th Oct
        self.overtime_amount = self.overtime_hours * (salary / 50)
        self.department = department
    def display_emp(self):
        return (f"Employee(ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}, "
                f"Overtime Hours: {self.overtime_hours}, Overtime Amount: {self.overtime_amount}, "
                f"Department: {self.department})")
employees = [
(Employee('E7876', 'ADAMS', 50000, 50, 'ACCOUNTING')),
(Employee('E7499', 'JONES', 45000, 45, 'RESEARCH')),
(Employee('E7900', 'MARTIN', 50000, 50, 'SALES')),
(Employee('E7698', 'SMITH', 55000, 55, 'OPERATIONS'))
]
for emp in employees:
    print(emp.display_emp())


# 7. Write a Python class BankAccount with attributes like account_number, balance,
# date_of_opening and customer_name, and methods like deposit, withdraw, and
# check_balance.
class BankAcc:
    def __init__(self):
        self.Acc_No=123412341234
        self.Balance=float(50000)
        self.Dof='20/10/2024'
        self.Cust_Name='Soham Karandikar'
    def display_details(self):
        return (f'Account No:      {self.Acc_No}\nDate Of Opening: {self.Dof}'
                f'\nCustomer Name:   {self.Cust_Name}\nBalance:         {self.Balance}')
    def transaction(self):
        while True:
            quest=input("Enter d for deposit and w for withdraw : ")
            if quest.lower()=='d':
                dep=float(input("Enter the amount you want to deposit : "))
                self.Balance=self.Balance+dep
                break
            elif quest.lower()=='w':
                wit=float(input("Enter the amount you want to withdraw : "))
                self.Balance=self.Balance-wit
                break
            elif quest.lower()!='d' or quest.lower()!='w':
                print("Invalid Input, Please try again!")
        print('The new balance is:',self.Balance)
banker=BankAcc()
print(banker.display_details())
banker.transaction()


# 8. Create a class hierarchy for different types of geometric shapes, including circles,
# rectangles, and triangles, using inheritance.
class shapes:
    def __init__(self):
        self.colour=''
        self.area=0
        self.peri=0
    def display(self):
        print(self.colour,'\n',self.area,'\n',self.peri)
class circle(shapes):
    def __init__(self,r):
        pi=3.14
        self.colour='Red'
        self.area=pi*(r**2)
        self.peri=2*pi*r
class triangle(shapes):
    def __init__(self,b,h,s1,s2,s3):
        self.colour='Blue'
        self.area=0.5*b*h       
        self.peri=s1+s2+s3
class rectangle(shapes):
    def __init__(self,s1,s2):
        self.colour='Green'
        self.area=s1*s2
        self.peri=2*(s1+s2)
class square(rectangle):
    def __init__(self, s1):
        self.colour='Orange'
        self.area=s1*s1
        self.peri=4*s1
class parallelogram(rectangle):
    def __init__(self, side, base,h):
        self.colour='Yellow'
        self.area=h*base
        self.peri=2*(side+base)
circ=circle(3)
tri=triangle(3,3,3,4,4)
rect=rectangle(4,5)
squ=square(4)
par=parallelogram(4,4,4)
circ.display()
tri.display()
rect.display()
squ.display()
par.display()


# 9. Create a Bus child class that inherits from the Vehicle class. The default fare charge of any 
# vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full
# fare as a maintenance charge. So total fare for bus instance will become the 
# final amount = total fare + 10% of the total fare.
# Note: The bus seating capacity is 50. so the final fare amount should be 5550.
# You need to override the fare() method of a Vehicle class in Bus class.
class vehicle:
    def __init__(self,seatcap):
        self.vfare=100*seatcap
    def display(self):
        print("The fare of the ride is:",self.vfare)
class bus(vehicle):
    def __init__(self,seatcap):
        self.vfare=100*seatcap + (10*seatcap)
output=bus(50)
output.display()
