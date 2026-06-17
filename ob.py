class Coaching :

        def __init__(self, name, age, course):
                self.name = name
                self.age = age
                self.course = course
                



        def details(self) :
                print(f"""
                        Student Details ===>
                            name : {self.name}
                            age : {self.age}
                            course : {self.course}""")



s1 = Coaching("Mehan", 16, "Python")
s1.details()
s2 = Coaching("Rohit",39, "Java")
s2.details()