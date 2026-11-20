

"""
==============================================================
 BioSkillz CodeStart — Python Foundations | Batch 01
 Task 01: Variables, Data Types, Input, Operators & Typecasting
==============================================================

 Name     : Ahmad Ammar
 Save as  : Ahmad_Ammar_task_01.py
 Deadline : Friday, 20 November 2026, 9:00 PM (PKT)
 Submit   : Upload this file to YOUR OWN GitHub repository.
"""


# ==============================================================
# PART A: SESSION EXERCISES
# ==============================================================

# --------------------------------------------------------------
# Exercise 1
# --------------------------------------------------------------

print(7 / 2)  # Divides 7 by 2

print(7 // 2)  # Floor division

print("7" + "2")  # Joins two strings

print(type(7.0))  # Shows the data type

print(2 + 3 * 4 ** 2)  # Uses arithmetic operators

print(bool("0"))  # Converts string into boolean


# --------------------------------------------------------------
# Exercise 2
# --------------------------------------------------------------

# Taking the user's name as input
name = input("Name: ")
print("Name:", name)

# Converting age into integer for calculation
age = int(input("Age: "))
print("Next Year:", age + 1)

print("Done")


# --------------------------------------------------------------
# Exercise 3
# --------------------------------------------------------------

total_bill = int(input("Input the total bill (in rupees): "))
no_of_friends = int(input("How many friends are paying: "))

print("====== Bill Distributor ======")
print("Total bill:", total_bill)
print("Number of friends:", no_of_friends)
print("Each pays:", total_bill // no_of_friends)
print("Left over:", total_bill % no_of_friends)


# ==============================================================
# PART B: TASKS
# ==============================================================

# --------------------------------------------------------------
# Task 1: Variables and Data Types
# --------------------------------------------------------------

# Store personal information in different data types.

name = "Ahmad Ammar"
age = 22
height = 1.8034
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))


# --------------------------------------------------------------
# Task 2: Temperature Converter
# --------------------------------------------------------------

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("Fahrenheit:", fahrenheit)
print("Kelvin:", kelvin)


# --------------------------------------------------------------
# Task 3: Simple Calculator
# --------------------------------------------------------------

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Power:", num1 ** num2)


# --------------------------------------------------------------
# Task 4: Savings Tracker
# --------------------------------------------------------------

savings = 1000

print("Starting savings:", savings)

savings += 500
print("After gift:", savings)

savings -= 300
print("After buying books:", savings)

savings *= 2
print("After doubling:", savings)


# --------------------------------------------------------------
# Task 5: Scholarship Check
# --------------------------------------------------------------

marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))

marks_check = marks >= 80
attendance_check = attendance >= 75

qualifies = marks_check and attendance_check

print("Marks 80 or more:", marks_check)
print("Attendance 75% or more:", attendance_check)
print("Qualifies for scholarship:", qualifies)


# ==============================================================
# Before you submit, check that:
#   [ ] Your name is written at the top of this file
#   [ ] The file is saved as name_task_01.py
#   [ ] The whole file runs without errors
#   [ ] Your output matches the examples
# ==============================================================
