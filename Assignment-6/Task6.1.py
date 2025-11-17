class Student:
    def __init__(self, name, student_id, age, course):
     
        self.name = name
        self.student_id = student_id
        self.age = age
        self.course = course
    
    def display_details(self):
        """
        Method to display all student details.
        """
        print("Student Details:")
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")


# Main program
if __name__ == "__main__":
    # Take input from user
    print("Enter Student Details:")
    print("-" * 30)
    
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    age = int(input("Enter student age: "))
    course = input("Enter course/major: ")
    
    # Create a student object with user input
    student = Student(name, student_id, age, course)
    
    print("\n" + "="*30 + "\n")
    
    # Display student details
    student.display_details()
