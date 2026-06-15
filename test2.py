grade_book = {
    "Alice"  : 90,
    "Sara" : 95,
    "Rahul"  : 80,
    "Rohit"  : 97,
    "Khushi"  : 96
}
total = 0
for i in grade_book.values() :
    total = total + i
average = total/5
print("Class Average : ", average)

top_student = max(grade_book, key=grade_book.get)
bottom_student = min(grade_book, key=grade_book.get)

print("The top student : ", top_student)
print("The bottom student : ", bottom_student)

name  = input("Enter name : ")
score  = grade_book.get(name, "student not found")
print(score)




