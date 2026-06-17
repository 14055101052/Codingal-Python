import array as arr

a = arr.array("i", [1,2,3])
print("\n The new array created : ", end = " ")
for i in range(0,3) :
    print(a[i], end =  " ")
print()

b = arr.array("d", [2.5,2.8,3.1])
print("\n The new array created : ", end = " ")
for i in range(0,3) :
    print(b[i], end =  " ")
print()

a.insert(1,4)
print("\n Array after insertion : ", end = " ")
for i in (a) : 
    print(i, end = " ")
print()

b.append(4.5)
print("\n Array after insertion : ", end = " ")
for i in (b) : 
    print(i, end = " ")
print()

print("Access element : ", a[0])
print("Access element : ", b[2])