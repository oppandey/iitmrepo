numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)#tuple of numbers
squares = []#list to hold squares

def func1():
    for n in numbers:
        squares.append(n ** 3)#Lambda function to compute cube
    return squares

def func2():
    return [n ** 3 for n in numbers]#Comprehension

def useYield():
    for n in numbers:
        yield n ** 3#Generator function

#print(func1())
#print(func2())

useYield_gen = useYield()
for val in useYield_gen:
    print(val)