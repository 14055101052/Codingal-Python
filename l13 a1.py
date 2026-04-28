print("\nSquare Pattern")
for i in range(1,4):
    for j in range(1,4):
        print("*", end= " ")
    print()

print("\nSquare Pattern")
n = 4 
for i in range(n):
    for j in range(n):
        print("*", end= " ")
    print()

print("\nRA Triangle")
n = 5
for i in range(n):
    for j in range(i + 1):
        print("*", end= " ")
    print()

print("\nInverted RA Triangle")
n = 5 
for i in range(n):
    for j in range(n - i):
        print("*", end= " ")
    print()

print("\nPyramid")
n = 5
for i in range(n):
    for s in range(n - i - 1):
        print(" ", end= " ")
    for j in range(2*i+1):
        print("*", end= " ")
    print()

print("\nDiamond")
n = 5 
for i in range(n):
    for s in range(n - i - 1):
        print(" ", end= " ")
    for j in range(2*i+1):
        print("*", end= " ")
    print()

for i in range(n - 2, - 1, - 1):
    for s in range(n - i - 1):
        print(" ", end= " ")
    for j in range(2*i+1):
        print("*", end= " ")
    print()