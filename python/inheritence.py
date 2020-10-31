#!/usr/bin/env python3
class person:
    name=""
    age=0
    def __init__ (self,personName,personAge):
        self.name=personName
        self.age=personAge
    
    def showName(self):
        print("My Name is "+self.name)
     
    def showAge(self):
        print("My Age is "+self.age)

class Student(person):
    studentId=""

    def __init__ (self, studentName,studentAge, studentId):
        person .__init__(self,studentName, studentAge)
        self.studentId=studentId

    def getId(self):
        return self.studentId

person1 = person("manish", "23")
person1.showName()
person1.showAge()
student1=Student("jay","22","102")
print(student1.getId())
student1.showName()
