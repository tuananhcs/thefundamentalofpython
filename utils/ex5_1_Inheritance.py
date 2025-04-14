#Class con kế thừa những thuộc tính từ class cha


# Định nghĩa một Class đơn giản "Person"
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

# Kế thừa từ Class "Person" để tạo Class "Student"
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)   # Gọi phương thức khởi tạo của lớp cha
        self.student_id = student_id

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}"

# Tạo một đối tượng thuộc Class "Person"
person1 = Person("Alice", 30)
print(person1.get_details())

# Tạo một đối tượng thuộc Class "Student"
student1 = Student("Bob", 25, "S123")
print(student1.get_details())