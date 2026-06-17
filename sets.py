fruits = {"apple", "banana", "cherry", "apple", "banana"}
print(fruits)
fruits.add("pineapple")
print("Fruits after adding : ", fruits)
fruits.remove("banana")
print("Fruits after removing : ", fruits)


num = {1,3,2,4,5,2,1}
print(num)
num.add(6)
print("After adding 6  : ", num)
num.remove(3)
print("After removing 3: ", num)


set1 = {1,2,3}
set2 = {3,4,5}

print("Union : ",set1.union(set2))

print("Intersection :", set1.intersection(set2))

print("Difference (set1 - set2) :", set1.difference(set2))