math = float(input("Please enter your Math marks : "))
english = float(input("Please enter your English marks : "))
social_science = float(input("Please enter your Social Science marks : "))
science = float(input("Please enter your Science marks : "))
french = float(input("Please enter your French marks : "))

total = math + english + social_science + science + french
print("Total marks obtained : ", total)

avg = total / 5
print("Average of the total marks : ", avg)

if avg > 100 or avg < 0:
    print("Invalid input !!")

elif avg >= 91 and avg <= 100:
    print("Your Grade is A1")

elif avg >= 81 and avg <= 90:
    print("Your Grade is A2")

elif avg >= 71 and avg <= 80:
    print("Your Grade is B1")

elif avg >= 61 and avg <= 70:
    print("Your Grade is B2")

elif avg >= 51 and avg <= 60:
    print("Your Grade is C1")

elif avg >= 41 and avg <= 50:
    print("Your Grade is C2")

elif avg >= 31 and avg <= 40:
    print("Your Grade is D1")

elif avg >= 21 and avg <= 30:
    print("Your Grade is D2")

elif avg >= 11 and avg <= 20:
    print("Your Grade is E")

else:
    print("Need Improvement !!!")