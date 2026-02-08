def useProgramBasics():
    print("Welcome to the Basic Python Console Application!")
    name = input("Enter your name: ")
    print(f"Hello, {name}! Have a great day.")
    age = input("Enter your age: ")
    age = int(age)

    if age > 18:  
        print("You are an adult.")
    else:
        print(f"You are {age} years old.")
    score = 85
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    else:
        grade = 'F'
    print(f"Your score is {score}, which corresponds to a grade of {grade}.")

def useFileHandling():
    #filename = "d:/sample.txt"
    #with open(filename, 'w') as file:
    #    file.write("This is a sample text file.\n")
    #    file.write("It contains multiple lines of text.\n")
    file = open("d:/sample.txt", 'r')
    content = file.readlines()
    print(content)
    file.close()

def useclasses():
    from employee import Employee, Manager
    emp = Employee("Alice", 70000)
    emp.display_info()

    mgr = Manager("Bob", 90000, "IT")
    mgr.display_info()


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

    for num in fibonacci(10):
        print(num)  

#def main():  
    #useProgramBasics()
    #useFileHandling()
    #useclasses()
    #squares = [x**2 for x in range(10)] 
    #print(squares)
    #fibonacci(10)

def useLangBasics():
	print("Welcome to Functions")
	name = input("Enter your name:")
	print(f"Welcome to Python Mr/Ms{name}")
	age = input("Enter your age:")
	print(f"Your age is {age}")
	age = int(age)
	if(age<0 or age>80):
		print("Invalid age")
	elif(age>=18):
		print("You are eligible to Vote")
	elif(age<18):
		print("You are not eligible to vote")

import math
import datetime
def useMath():
    print(math.sqrt(16))
    print(datetime.datetime.today())

def main():
    print("Hello World")
    #Hello
    useMath()

if __name__ == "__main__":
	main()