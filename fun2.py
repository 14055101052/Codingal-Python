def add(a,b):
    return(a+b)
def subtarct(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)
def modules(a,b):
    return(a%b)

print("Please select the operation")
print("a.Add")
print("b.Subtract")
print("c.Multiply")
print("d.Divide")
print("e.Modules")

choice = input("Please enter choice (a/b/c/d/e) : ")
num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))

if choice == "a":
    print(f"{num1} + {num2} = ", add(num1,num2))
elif choice == "b":
     print(f"{num1} - {num2} = ", subtarct(num1,num2))
elif choice == "c":
     print(f"{num1} * {num2} = ", multiply(num1,num2))
elif choice == "d":
     print(f"{num1} / {num2} = ", divide(num1,num2))
elif choice == "e":
     print(f"{num1} % {num2} = ", modules(num1,num2))
else : 
    print("Invalid !!!")