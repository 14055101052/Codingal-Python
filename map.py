num1 = [1,2,3]
num2 = [2,4,6]

result = map(lambda x , y : x + y, num1, num2)
print("Addition of two lists")
print(list(result))


num = [1,2,3,4,5,6]
def sq(x):
    return x*x
result = map(sq,num)
print("The square of the numbers")
print(list(result))