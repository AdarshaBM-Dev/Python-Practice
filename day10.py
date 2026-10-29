# While Loop Practice

# Topics: while, break, continue, sums, nested loops, patterns, PIN verification


# 1. Print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1


# 2. Print numbers from 1 to 5, increasing by 2
i = 1
while i <= 5:
    print(i)
    i += 2


# 3. Reverse counting from 5 to 1
i = 5
while i >= 1:
    print(i)
    i -= 1


# 4. Stop the loop when i becomes 4 (break)
i = 1
while i <= 5:
    if i == 4:
        break
    print(i)
    i += 1


# 5. Skip the number 3 (continue)
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)


# 6. Find the sum of numbers from 1 to 4
i = 1
total = 0
while i <= 4:
    total += i
    i += 1
print(total)


# 7. Find the sum of even numbers from 1 to 5
i = 1
total = 0
while i <= 5:
    if i % 2 == 0:
        total += i
    i += 1
print(total)


# 8. Nested while loop: print i and j (i: 1-2, j: 1-3)
i = 1
while i <= 2:
    j = 1
    while j <= 3:
        print(i, j)
        j += 1
    i += 1


# 9. Nested while loop: print i and j (both: 1-2)
i = 1
while i <= 2:
    j = 1
    while j <= 2:
        print(i, j)
        j += 1
    i += 1


# 10. Print a star three times for each outer-loop iteration
# Note: print("*") puts each star on a separate line.
i = 1
while i <= 2:
    j = 1
    while j <= 3:
        print("*")
        j += 1
    i += 1


# 11. Print the outer-loop value three times per iteration
i = 1
while i <= 2:
    j = 1
    while j <= 3:
        print(i)
        j += 1
    i += 1


# 12. Nested while loop practice (same pattern as example 8)
i = 1
while i <= 2:
    j = 1
    while j <= 3:
        print(i, j)
        j += 1
    i += 1


# 13. PIN verification: keep asking until the correct PIN is entered
correct_pin = "1234"
entered_pin = ""

while entered_pin != correct_pin:
    entered_pin = input("Enter PIN: ")
    if entered_pin != correct_pin:
        print("Wrong PIN. Try again.")

print("PIN accepted!")


# 14. PIN verification with a maximum of 3 attempts
correct_pin = "1234"
entered_pin = ""
trials = 1

while entered_pin != correct_pin and trials <= 3:
    entered_pin = input(f"Attempt {trials} - Enter PIN: ")
    trials += 1

    if entered_pin != correct_pin:
        print("Wrong PIN. Try again.")

if entered_pin == correct_pin:
    print("PIN accepted!")
else:
    print("Too many attempts!")
