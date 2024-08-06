# Question no 1
# write a pyhton program that prints "hello World!" to the console
print("Hello, World!")

# Question no 2
# Create Variables to store your name,age and favorite hobby,print these variables
x="Komal Siddharth"
y=21
z="my hobby is to read books"
print(x)
print(y)
print(z)

# Question no 3
# Add comments to your code explainig what each line does
x="Komal Siddharth"  # here we declare a variable named x to store the string consisting name
y=21    # here an variable y is declared to store the age
z="my hobby is to read books"  # here variable z is declared to store hobby
print(x) # print function print the variable x
print(y) # print function print the variable y 
print(z) # print function print the variable z

#Question no 4
# write a program that takes an integer as an input from the user and print whether the number is positive,negative or zero
x=float(input("Enter the number: "))
if x>0:
 print("it is a positive number")
elif x==0:
 print("it is a zero")
else:
  print("it is a negative number")

# Question no 5
# create aprogram to check whether it is a leap year or not
# we define a function named leapyear to check the condition for leap yaer
def leapYear(year):  
 return (year%4==0 and year%100!=0) or (year%400==0)
year_check=2023  #year to be checked 
result=leapYear(year_check)  # result variable to store the answer
print(f"{year_check} is a leap year: {result}")

# Question no 6
# write a program that prints the first 10 natural numbers using a for loop
# i=1
for i in range(1,11):
 print(i)

# Question no 7
# create a program  that prints the multiplication table of a given nnumber using while loop
a=2
i=1
while(i<=10):
 result=a*i
 print(f"{a} x {i} = {result}")
 i+=1

# Question no 8
#  write aprogram that iterates through numbers from 1 to 10 and print each number.use the continue statement
# to skip numbers that are divisible by 3
for i in range(1,11):
 if(i%3==0):
  continue
 else:
  print(i)

# Question no 9
# create a program that stop printing when it encounters an number greater than 5using the break statement
for i in range(1,11):
 if(i>5):
  break
 else:
  print(i)

# Question no 10
# define afunction called greet takes a name as an argument and prints"Hello,[name]!
# name=input("enter your name: ")
def greet(name):
 print("hello,"+name+"!")
greet("komal")
 
# Question no 11
# create afunction that takes numbers as arguments and returns their sum
# num1=input("enter your first number: ")
# num2=input("enter your first number: ")
def sum(num1,num2):
 print(num1+num2)
sum(2,4)

