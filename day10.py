#  While Loop

# 1. Print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# 2. Print numbers from 5 to 1
i = 5
while i >= 1:
    print(i)
    i -= 1

# 3. Print even numbers from 1 to 10
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

# 4. Print odd numbers from 1 to 10
i = 1
while i <= 10:
    if i % 2 == 1:
        print(i)
    i += 1

# 5. Stop the loop using break
i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1

# 6. Skip number 3 using continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 7. Sum of numbers from 1 to 5
i = 1
total = 0
while i <= 5:
    total = total + i
    i += 1
print("Sum:", total)

# 8. Sum of even numbers from 1 to 10
i = 1
total = 0
while i <= 10:
    if i % 2 == 0:
        total = total + i
    i += 1
print("Even sum:", total)

# 9. PIN verification example
correct_pin = "1234"
entered_pin = ""

while entered_pin != correct_pin:
    entered_pin = input("Enter PIN: ")
    if entered_pin != correct_pin:
        print("Wrong PIN. Try again.")

print("PIN accepted!")

# 10. Nested while loop
row = 1
while row <= 3:
    col = 1
    while col <= 2:
        print("Row:", row, "Column:", col)
        col += 1
    row += 1
