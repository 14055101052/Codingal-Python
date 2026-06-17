friends = ("Rohit","Kohli","Dhoni","Rohit")
print("Good Friend : ", friends[0])

print(friends.count("Rohit"))
print(friends.index("Rohit"))
print("First two friends : ", friends[0:2])
print("Last two friends : ", friends[-2])

count = 0
for i in friends :
    print(f"Friend {count} : ", i)
    count = count + 1




tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

tuplex = (4,6,2,8,1,5)
tuplex = tuplex + (9,)
print(tuplex)


tuplex = (20,30,40,50,60,70)
print(tuplex.count(50))

tuplex = (2,4,6,8,10,12,14,16)
slice = tuplex[3:5]
print(slice)
slice = tuplex[:6]
print(slice)