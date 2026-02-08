def main():
    from Employee import Employee

    emp1 = Employee("Alice", "Developer", 70000)
    emp2 = Employee("Bob", "Designer", 65000)
    emp3 = Employee("Charlie", "Tester", 60000)

    print(emp1.get_details())
    print(emp2.get_details())
    print(emp3.get_details())

if __name__ == "__main__":
    main()