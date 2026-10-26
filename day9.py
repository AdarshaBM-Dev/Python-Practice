#  Conditional Statements

# 1. if statement
age = 20

if age >= 18:
    print("Eligible to vote")


# 2. if-else statement
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")


# 3. if-elif-else statement
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")


# 4. Comparison operators in conditions
number = 10

if number != 10:
    print("Number is different")
else:
    print("Number is 10")


# 5. Logical AND operator
age = 25

if age >= 18 and age <= 60:
    print("Eligible")
else:
    print("Not eligible")


# 6. Logical OR operator
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")


# 7. Logical NOT operator
is_raining = False

if not is_raining:
    print("You can go outside")
else:
    print("Take an umbrella")


# 8. Nested if statement
day = "Sunday"
raining = True

if day == "Sunday":
    if raining:
        print("Stay home")
    else:
        print("Go outside")
else:
    print("Go to work")


# 9. Indentation example
age = 17

if age >= 18:
    print("Adult")
else:
    print("Minor")


# 10. match-case statement (Python 3.10+)
color = "red"

match color:
    case "red":
        print("Red color")
    case "blue":
        print("Blue color")
    case _:
        print("Unknown color")


# 11. Grade calculation using elif
marks = 35

if marks >= 90:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 40:
    print("C")
else:
    print("Fail")


# 12. User input example
student_marks = int(input("Enter your marks: "))

if student_marks >= 90:
    print("Grade A")
elif student_marks >= 75:
    print("Grade B")
elif student_marks >= 60:
    print("Grade C")
elif student_marks >= 40:
    print("Pass")
else:
    print("Fail")
