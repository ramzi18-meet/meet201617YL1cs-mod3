class Student:
    def __init__(self, student_name, hair, height):
        self.name = student_name
        self.hair = hair
        self.height= height


s1 = Student('Ramzi', 'Black', '160')
s2=Student('Yazan', 'Brown', '127')


print(s1.name, s1.height)
print(s2.name, s2.hair)
