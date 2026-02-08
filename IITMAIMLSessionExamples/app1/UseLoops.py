names = ("Ganesh","Mahesh","Suresh","Ramesh")
for name in names:
    print(f"Hello, {name}!")

for i in range(1, 10):
    print(f"Square of {i} is {i*i}")

count = 1 #initialization
while   count <= 10: #condition
    print(f"Square of {count} is {count*count}")
    count += 1 #increment

for i in range(1, 10):
    if i % 2 == 0:
        print(f"{i} is Even")