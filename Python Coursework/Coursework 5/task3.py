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

        Employee.counter += 1
        self._salary = salary
        self.__employee_id = f"EMP{Employee.counter:02d}"

    def __del__(self):
        Employee.counter -= 1

    @property
    def employee_count(self):
        return Employee.counter

    def get_employee_id(self):
        return self.__employee_id

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        self._salary = new_salary

    def increase_salary(self, amount):
        self._salary += amount

    def decrease_salary(self, amount):
        self._salary -= amount

    def introduce(self):
        print(f"Hello, my name is {self.name} and I work as an employee.")

# -------------------- Teacher Class --------------------
class Teacher(Employee):
    counter=0
    
    def __init__(self,name, age, gender, address, salary):
        super().__init__(name, age , gender, address, salary)
        
        # Increment teacher counter
        Teacher.counter+=1
        
        # Initialize subjects list
        self.subjects=[]
        
        # Private teacher ID
        self.__teacher_id=f"TEC{Teacher.counter:02d}"
    #Destructor  
    def __del__(self):
        Teacher.counter-=1
        super().__del__()
        
    #Teacher Count Ptroperty   
    @property
    def teacher_count(self):
        return Teacher.counter
    
    # Getter for teacher ID   
    def get_teacher_id(self):
        return self.__teacher_id
    
    # Subject managemen    
    def add_subject(self, subject):
        self.subjects.append(subject)
        
    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)
    # Override introduce    
    def introduce(self):
        subjects_str=", ".join(self.subjects)
        print(f"My ID is {self.__teacher_id} and i teach: {subjects_str}.")
    # Override employee_id access   
    def get_employee_id(self):
        raise AttributeError(f"{self.__class__.__name__} object has no attribute 'employee id'")

# -------------------- Main Execution --------------------
if __name__ == "__main__":
    teacher1 = Teacher("Simran", 35, "Female", "Amritsar", 70000)

    # Add subjects
    teacher1.add_subject("Mathematics")
    teacher1.add_subject("Physics")

    # Introduce
    teacher1.introduce()

    # Print details
    print(teacher1)

    # Teacher ID
    print("Teacher ID:", teacher1.get_teacher_id())

    # Teacher count
    print("Teacher Count:", teacher1.teacher_count)

    # Try accessing employee_id (should raise error)
    try:
        teacher1.get_employee_id()
    except AttributeError as e:
        print(e)   
        