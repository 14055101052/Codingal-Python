friends = ["Mehan","Rohit","Gaurav","Kohli","Ram"]
print(friends)

print("The friend who is good at math : ", friends[0])
print("The friend who is good at englsih : ", friends[1])
print("The friend who is good at computer : ", friends[2])
print("The friend who is good at sports : ", friends[3])
print("The friend who is good at science : ", friends[4])

friends[2] = "Tarab"
print(friends)

friends.append("Ajeet")
print(friends)

friends.remove("Ram")
print(friends)

count = 1
for i in friends :
    print(f"Friend number {count} : ",i)
    count = count + 1