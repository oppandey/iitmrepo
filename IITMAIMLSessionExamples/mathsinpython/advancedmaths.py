from basicmaths import factorial

def permutation(n, r):
    if r > n:
        return 0
    return factorial(n) // factorial(n - r)

def combination(n, r):
    if r > n:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

def binomial_coefficient(n, k):
    return combination(n, k)

def pascals_triangle(rows):
    triangle = []
    for n in range(rows):
        row = []
        for k in range(n + 1):
            row.append(binomial_coefficient(n, k))
        triangle.append(row)
    return triangle

#print("This is advancedmaths.py in mathsinpython package")
#print("5P2 is:", permutation(5, 2))
#print("5C2 is:", combination(5, 2))
#print("Binomial Coefficient C(5,2) is:", binomial_coefficient(5, 2))
print("Pascal's Triangle with 5 rows:", pascals_triangle(5))    