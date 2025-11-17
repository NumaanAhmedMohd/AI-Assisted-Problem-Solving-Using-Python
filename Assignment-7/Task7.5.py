# Faulty code - accessing invalid list index
numbers = [1, 2, 3]
try:
    print(numbers[5])  # ERROR: IndexError - list index out of range
except IndexError:
    print("Index out of range")

