# def sum(a,b):
#     print("Sum : ", a + b)

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# sum(num1,num2)

# def count(n):
#     if n == 0 :
#         return 
#     print(n)
#     count(n - 1)

# count(5)

def factorial(n):
    if n == 1 :
        return 1
    return n * factorial(n - 1)
ans = factorial(5)
print("The factorial of 5 : ", ans)