a = "Mehan"
print(a[0])
print(a[0 : 4])
print(a[::-1])

u = a.upper()
l = a.lower()
print("upper case :", u)
print("lower case :", l)

ans = input("Do you play cricket?")
if ans.lower() == "yes" :
    print("Who is your favourite player?")
else :
    print("Which sport do you play?")