def basic_ops():
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = num1/num2
            return result
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception: #Generic Error Handler
            print("Error")
        finally:
            print("Finally block executed")#closure activities

print(f"Result is {basic_ops()}")