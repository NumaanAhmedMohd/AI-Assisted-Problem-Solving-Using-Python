class sru_student:
    # Class definition for managing student information and academic fees
    
    def __init__(self, name, roll_no, hostel_status):
        # Initialize instance with name, roll number, and hostel status
        self.name = name  # Assign name parameter to instance variable
        self.roll_no = roll_no  # Assign roll_no parameter to instance variable
        self.hostel_status = hostel_status  # Assign hostel_status parameter to instance variable
        self.fee_amount = 0  # Initialize fee_amount to zero
    
    def fee_update(self, base_fee):
        # Calculate and update student fee based on hostel status
        if self.hostel_status:
            # If student is in hostel, add hostel charges to base fee
            self.fee_amount = base_fee + 2500
        else:
            # If student is not in hostel, set fee to base fee only
            self.fee_amount = base_fee
        
        return self.fee_amount  # Return the calculated fee amount
    
    def display_details(self):
        # Display student information in formatted output
        print("=" * 50)  # Print a separator line
        print(f"Name: {self.name}")  # Display student name
        print(f"Roll No.: {self.roll_no}")  # Display student roll number
        if self.hostel_status:
            # If hostel status is true, display hostel resident
            print(f"Hostel Status: Yes (Resident)")
        else:
            # If hostel status is false, display day scholar
            print(f"Hostel Status: No (Day Scholar)")
        print(f"Fee Amount: Rs. {self.fee_amount}")  # Display fee amount in rupees
        print("=" * 50)  # Print a separator line


# Create and manage student objects
if __name__ == "__main__":
    # Execute this block only when script is run directly
    student1 = sru_student("Rahul Kumar", 101, True)  # Create first student object
    student1.fee_update(50000)  # Update fee for first student with base fee 50000
    student1.display_details()  # Display details of first student
    
    student2 = sru_student("Priya Sharma", 102, False)  # Create second student object
    student2.fee_update(50000)  # Update fee for second student with base fee 50000
    student2.display_details()  # Display details of second student
    
    student3 = sru_student("Anil Patel", 103, True)  # Create third student object
    student3.fee_update(50000)  # Update fee for third student with base fee 50000
    student3.display_details()  # Display details of third student
