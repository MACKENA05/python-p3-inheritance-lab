#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name,knowledge=[]):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge
    
    def learn(self, new_knowledge):
        return self.knowledge.append(new_knowledge)



student1 = Student('John', 'Doe')
print(student1.first_name)
print(student1.learn('Python programming'))
print(student1.knowledge)