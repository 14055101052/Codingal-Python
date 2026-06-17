try : 
    num1 = int(input("Enter number : "))
    num2 = int(input("Enter number : "))
    result = num1/num2
    print("Result is : ", result)
    print("Result is : ", result1)

except ZeroDivisionError : 
    print("Divison be zero is not allowed")
except ValueError:
    print("Please print a numerical value")
except NameError as ex:
    print(f"The exception is {ex}")
except :
    print("Something went wrong")
finally : 
    print("I will execute no matter what happens")