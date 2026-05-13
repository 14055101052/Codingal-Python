name = input("Enter your name : ")
for i in name:
    if(i.lower() == "a"):
        print("A is found")
        break
    else : 
        print("A is not found")


for x in range(10):
    if x % 20 == 0:
        print("twist")
    if x % 15 == 0:
        pass
    if x % 5 == 0:
        print("fizz")
    if x % 3 == 0:
        print("buzz")
    else : 
        print(x)

i = 10
while(i > 0):
    i = i - 1
    if i == 5 :
        continue
    print("the value of i : ", i)
print("Good Bye")