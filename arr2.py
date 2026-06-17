import array as arr

num = arr.array("i", [1,3,5,3,6,7,3])
print("Original Array : " +str(num))

print("Number of occurencesof number 3 in the array : " +str(num.count(3)))


num.reverse()
print("Reverse of the array : " +str(num))