from abc import ABC, abstractmethod

# -------------------- Person Class --------------------
class Person(ABC):
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}"

    def greet(self, other_person):
        print(f"Hello {other_person.name}! My name is {self.name}.")

    @abstractmethod
    def introduce(self):
        pass

    @staticmethod
    def is_adult(age):
        return age >= 18


# -------------------- Employee Class --------------------
class Employee(Person):
    counter = 0

    def __init__(self, name, age, gender, address, salary):
        super().__init__(name, age, gender, address)

        # Increment counter
        Employee.counter += 1

        # Protected attribute
        self._salary = salary

        # Private attribute 
        self.__employee_id = f"EMP{Employee.counter:02d}"

    # Destructor
    def __del__(self):
        Employee.counter -= 1

    # Property for counter
    @property
    def employee_count(self):
        return Employee.counter

    # Getter for employee ID (no setter)
    def get_employee_id(self):
        return self.__employee_id

    # Salary Getter
    def get_salary(self):
        return self._salary

    # Salary Setter
    def set_salary(self, new_salary):
        self._salary = new_salary

    # Increase Salary
    def increase_salary(self, amount):
        self._salary += amount

    # Decrease Salary
    def decrease_salary(self, amount):
        self._salary -= amount

    # Override introduce method
    def introduce(self):
        print(f"Hello, my name is {self.name} and I work as an employee.")


# -------------------- Main Execution --------------------
if __name__ == "__main__":
    emp1 = Employee("John", 30, "Male", "Delhi", 50000)
    emp2 = Employee("Alice", 25, "Female", "Bathinda", 60000)

    # Test greet
    emp1.greet(emp2)

    # Test introduce
    emp1.introduce()

    # Test __str__
    print(emp1)

    # Test employee ID
    print("Employee ID:", emp1.get_employee_id())

    # Test salary methods
    print("Salary:", emp1.get_salary())
    emp1.increase_salary(5000)
    print("After increment:", emp1.get_salary())
    emp1.decrease_salary(2000)
    print("After decrement:", emp1.get_salary())

    # Test static method
    print("Is adult:", Person.is_adult(20))

    # Test employee counter
    print("Employee Count:", emp1.employee_count)