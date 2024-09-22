class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

        
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Creating an instance of the person class
person1 = Person("John Mutuma", 30, "Male")

# call the introduce method
person1.introduce()
