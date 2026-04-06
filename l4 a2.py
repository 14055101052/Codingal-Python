amount = int(input("Please enter the money withdrawn : "))

note_100 = amount//100
amount = amount%100
note_50 = amount//50
amount = amount%50
note_20 = amount//20
amount = amount%20

print("number of 100 notes : ", note_100)
print("number of 50 notes : ", note_50)
print("number of 20 notes : ", note_20)