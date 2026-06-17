student_data = {
    "id1" : {"name" : "Sara", "class" : "V", "subject integration" : "english,math,science"},
    "id2" : {"name" : "Rahul", "class" : "VI", "subject integration" : "english,hindi,science"},
    "id3" : {"name" : "Sara", "class" : "V", "subject integration" : "english,math,science"},
    "id4" : {"name" : "Rohit", "class" : "IV", "subject integration" : "french,math,science"}
}


result = {}
seen_keys = []

for student_id, details in student_data.items() :
    unique = (details["name"], details["class"], details["subject integration"])

    if unique not in seen_keys :
        seen_keys.append(unique)
        result[student_id]  = details

for k , v in result.items() :
    print(k, ":" , v)