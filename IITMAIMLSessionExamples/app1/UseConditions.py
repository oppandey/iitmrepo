global_var = 5000

def use_conditions(name, age):
#print("Welcome to Conditional Programming")
#name = input("Enter your name: ")
#age = int(input("Enter your age: "))

    if age < 0 or age > 80:
        return ("Invalid age entered.")
    elif age < 18:
        return (f"Hello {name}, you are a minor.")
    else:
        return (f"Hello {name}, you are an adult and eligible to vote.")

def check_number(number):
#print("Check if number is positive, negative or zero")
#number = int(input("Enter your number: "))
    #local variable
    local_var = 10000
    if number > 0:
        return (f"The number {number} is positive.")
        if number % 2 == 0:
            return (f"The number {number} is also even.")
        else:
            return (f"The number {number} is odd.")
    elif number < 0:
        return (f"The number {number} is negative.")
    else:
        return ("The number is zero.")

print(use_conditions("Test", 20))
print(check_number(10))
print(f"Global Variable: {global_var}") 
#print(f"Local Variable: {local_var}") # This will raise an error since local_var is not defined here   