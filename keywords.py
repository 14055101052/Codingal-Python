# return 
def sum(a,b):
    ans = a + b
    return ans

result = sum(10,20)
print("The sum of 10 and 20 : ", result)

# continue
for i in range(1,10):
    if i == 3 :
        continue
    print("the value of i : ", i)

# break
i = 10
while(i>=1):
    if i == 3:
        break
    print("the value of i : ", i)
    i = i - 1

# pass
def passFunction():
    pass