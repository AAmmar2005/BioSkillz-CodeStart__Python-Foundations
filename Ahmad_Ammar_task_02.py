
# ==============================================================
# BioSkillz CodeStart — Python Foundations | Batch 01
# Task 02: Strings & Conditional Statements
# Name: Ahmad Ammar
# Save as: ahmad_ammar_task_02.py
# ==============================================================


# ==============================================================
# PART A: SESSION EXERCISES
# ==============================================================

# --------------------------------------------------------------
# Exercise 1
# --------------------------------------------------------------

print("Python"[1:4])  # Prints characters from index 1 to 3

print("Banana".count("an"))  # Counts how many times "an" appears

print("Hello"[-1])  # Prints the last character

print("Zebra" > "Apple")  # Compares strings character by character

print(5 > 3 and 2 > 4)  # Both conditions must be True

print(not "")  # Empty string is False, and not reverses it to True


# --------------------------------------------------------------
# Exercise 2
# --------------------------------------------------------------

marks = int(input("Marks: "))

if marks >= 50:
    print("Pass")
else:
    print("Fail")

answer = input("Again? ")

if answer == "yes":
    print("Restarting...")


# --------------------------------------------------------------
# Exercise 3
# --------------------------------------------------------------

stuName = input("Please Enter your name: ").strip().title()

stuMarks_str = input("Please enter your marks (0-100): ")

# Check whether the input contains only digits
if not stuMarks_str.isdigit():
    print("Error: Please input a valid value (0-100).")

else:
    stuMarks = int(stuMarks_str)  # Converts string into integer

    print(f"Student name: {stuName}")
    print(f"Marks (0-100): {stuMarks}")

    if stuMarks > 100:
        print("Marks must be (0-100)")
    elif stuMarks >= 90:
        print(f"{stuName} scored {stuMarks}/100 -> Grade A")
    elif stuMarks >= 80:
        print(f"{stuName} scored {stuMarks}/100 -> Grade B")
    elif stuMarks >= 70:
        print(f"{stuName} scored {stuMarks}/100 -> Grade C")
    elif stuMarks >= 50:
        print(f"{stuName} scored {stuMarks}/100 -> Grade D")
    else:
        print(f"{stuName} scored {stuMarks}/100 -> Grade F")


# ==============================================================
# PART B: TASKS
# ==============================================================

# --------------------------------------------------------------
# Task 1: Name Formatter (String Methods)
# --------------------------------------------------------------

userName = input("Enter your full name: ")

print("Uppercase:", userName.upper())
print("Lowercase:", userName.lower())
print("Title case:", userName.title())
print("Total characters:", len(userName))
print("Number of 'a':", userName.lower().count("a"))


# --------------------------------------------------------------
# Task 2: Email Breakdown (Indexing and Slicing)
# --------------------------------------------------------------

userMail = input("Enter your email: ")

posA = userMail.find("@")

# Check that the email is not empty and contains @
if userMail != "" and posA != -1:

    firstCha = userMail[0]
    lastCha = userMail[-1]

    userName = userMail[:posA]
    domain = userMail[posA + 1:]

    isGmail = userMail.endswith("gmail.com")

    print("First character:", firstCha)
    print("Last character:", lastCha)
    print("Position of @:", posA)
    print("Username:", userName)
    print("Domain:", domain)
    print("Gmail address:", isGmail)

else:
    print("Please enter a valid email address.")


# --------------------------------------------------------------
# Task 3: Report Card (f-strings and Typecasting)
# --------------------------------------------------------------

userName = input("Enter your name: ")

s1Marks = float(input("Enter marks for Subject 1: "))
s2Marks = float(input("Enter marks for Subject 2: "))
s3Marks = float(input("Enter marks for Subject 3: "))

obtainMarks = s1Marks + s2Marks + s3Marks
totalMarks = 300

percentage = (obtainMarks / totalMarks) * 100

print("----- Report Card -----")
print(f"Name: {userName}")
print(f"Total: {obtainMarks} out of {totalMarks}")
print(f"Percentage: {percentage:.2f}%")


# --------------------------------------------------------------
# Task 4: Grade Calculator (if, elif and else)
# --------------------------------------------------------------

marks = int(input("Enter your marks (0-100): "))

if marks > 100 or marks < 0:
    print("Invalid marks")

elif 85 <= marks <= 100:
    grade = "A"
    print("Grade:", grade)

elif 70 <= marks <= 84:
    grade = "B"
    print("Grade:", grade)

elif 55 <= marks <= 69:
    grade = "C"
    print("Grade:", grade)

elif 40 <= marks <= 54:
    grade = "D"
    print("Grade:", grade)

else:
    grade = "F"
    print("Grade:", grade)


# --------------------------------------------------------------
# Task 5: Login Checker (Nested Conditions)
# --------------------------------------------------------------

userName = input("Enter username: ").strip().lower()
passWord = input("Enter password: ")

if userName == "codestart":

    if passWord == "python123":
        print("Login successful. Welcome to CodeStart!")

    else:
        print("Incorrect password. Please try again.")

else:
    print("Username not found.")

