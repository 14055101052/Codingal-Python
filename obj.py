Gaurav = {
    "name" : "Gaurav",
    "age" : 25,
    "course" : "HTML and CSS"
}

Mehan = {
    "name" : "Mehan",
    "age" : 16,
    "course" : "Python"
}

Rohit = {
    "name" : "Rohit",
    "age" : 15,
    "course" : "Java"
}



students = [Gaurav["name"],Mehan["name"],Rohit["name"]]
Mehan["course"] = "Java"
Mehan["School"] = "ABC SCHOOL"
del Mehan["age"]
print("Mehan object has been updated : ", Mehan)
print(students)
