try : 
    def add(a,b): 
        return (a + b)
    def subtract(a,b): 
        return (a - b)
    def multiply(a,b): 
        return (a * b)
    def divide(a,b): 
        return (a / b)
    
    num1 = float(input("Enter a number : "))
    num2 = float(input("Enter a number : "))

    choice = input("What operation would you like to carry(add/multiply/subtract/divide) : ")

    if choice.lower() == "add":
        print(f"The sum of {num1} and {num2} : ", add(num1,num2))
    if choice.lower() == "multiply":
        print(f"The multiplication of {num1} and {num2} : ", multiply(num1,num2))
    if choice.lower() == "subtract":
        print(f"The subtraction of {num1} and {num2} : ", subtract(num1,num2))
    if choice.lower() == "divide":
        print(f"The divison of {num1} and {num2} : ", divide(num1,num2))

except ValueError :
    print("Please print a numerical value")
except ZeroDivisionError :
    print(f"{num1} cannot be divide by zero")