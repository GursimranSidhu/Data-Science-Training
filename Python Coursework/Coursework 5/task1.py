from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, gender, address):
        # Initialize attributes
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    # Magic Method
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}"

    # greet method
    def greet(self, other_person):
        print(f"Hello {other_person.name}! My name is {self.name}.")

    # Abstract Method
    @abstractmethod
    def introduce(self):
        pass

    # Static Method
    @staticmethod
    def is_adult(age):
        return age >= 18


# Child Class
class User(Person):
    def __init__(self, name, age, gender, address):
        super().__init__(name, age, gender, address)

    def introduce(self):
        print(f"I am {self.name} from {self.address}.")


# Main Execution Block
if __name__ == "__main__":
    person1 = User("Alice", 20, "Female", "Bathinda")
    person2 = User("Mike", 25, "Male", "Delhi")

    person1.greet(person2)
    person1.introduce()
    print(person1)
    print(Person.is_adult(19))