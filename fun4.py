# def cube(number):
#     return number*number*number

# def by_three(number):
#     if number % 3 == 0 : 
#         return cube(number)
#     else : 
#         return False
    
# print(by_three(9))
# print(by_three(4))

def factorial(x):
   '''This is a recursive function to find a factorial of an integer'''
   if x == 1 or x == 0 :
       return 1
   else: 
       return x * factorial( x - 1)
   
print(factorial.__doc__)
print("The factorial of 5 : ", factorial(5))
print("The factorial of 4 : ", factorial(4))
print("The factorial of 3 : ", factorial(3))
print("The factorial of 2 : ", factorial(2))