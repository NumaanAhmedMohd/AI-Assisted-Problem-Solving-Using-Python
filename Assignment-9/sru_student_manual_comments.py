# Define the sru_student class to represent a student in the university
class sru_student:
    
    # Constructor to initialize student attributes
    def __init__(self, name, roll_no, hostel_status):
        # Store the student's name as an instance variable
        self.name = name
        # Store the student's roll number as an instance variable
        self.roll_no = roll_no
        # Store the hostel accommodation status (True/False) as an instance variable
        self.hostel_status = hostel_status
        # Initialize fee amount to 0; will be updated through fee_update method
        self.fee_amount = 0
    
    # Method to update the student's fee based on hostel status
    def fee_update(self, base_fee):
        # Check if student is living in hostel
        if self.hostel_status:
            # Add hostel charges (2500) to the base fee for hostel students
            self.fee_amount = base_fee + 2500
        else:
            # Use only base fee for day scholars (non-hostel students)
            self.fee_amount = base_fee
        
        # Return the calculated fee amount to the caller
        return self.fee_amount
    
    # Method to display all student details on the console
    def display_details(self):
        # Print a header for the student information
        print("=" * 50)
        # Print the student's name with label
        print(f"Name: {self.name}")
        # Print the student's roll number with label
        print(f"Roll No.: {self.roll_no}")
        # Check hostel status and print appropriate message
        if self.hostel_status:
            # Display that student is a hostel resident
            print(f"Hostel Status: Yes (Resident)")
        else:
            # Display that student is a day scholar
            print(f"Hostel Status: No (Day Scholar)")
        # Print the total fee amount with label
        print(f"Fee Amount: Rs. {self.fee_amount}")
        # Print a footer line for clarity
        print("=" * 50)


# Main program section - executed when script is run directly
if __name__ == "__main__":
    # Create first student object: Hostel resident
    student1 = sru_student("Rahul Kumar", 101, True)
    # Call fee_update method with base fee of 50000 for first student
    student1.fee_update(50000)
    # Display complete details of first student
    student1.display_details()
    
    # Create second student object: Day scholar
    student2 = sru_student("Priya Sharma", 102, False)
    # Call fee_update method with base fee of 50000 for second student
    student2.fee_update(50000)
    # Display complete details of second student
    student2.display_details()
    
    # Create third student object: Another hostel resident
    student3 = sru_student("Anil Patel", 103, True)
    # Call fee_update method with base fee of 50000 for third student
    student3.fee_update(50000)
    # Display complete details of third student
    student3.display_details()
