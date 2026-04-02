print("Welcome to mini Calculator✨")
print("This calculator can perform the following -")
print("""
1. Divison
2. Addition
3. Multiplication
4. Subtraction""")
num1 = int(input("Please enter a number : "))
num2 = int(input("Please enter a number : "))
ans = input("PLease select the operation you want to carry out : ")

if ans.lower() == "divide" or ans.lower() == "divison" :
    print(num1/num2)
elif ans.lower() == "add" or ans.lower() == "addition" :
    print(num1 + num2)
elif ans.lower() == "multiply" or ans.lower() == "multiplication" :
    print(num1*num2)
elif ans.lower() == "subtract" or ans.lower() == "subtraction" :
    print(num1 - num2)


