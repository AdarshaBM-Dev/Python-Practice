#  For Loops

# 1. Basic for loop
for i in range(1, 4):
    print("Hello")

# 2. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# 3. range() with step
for i in range(1, 6, 2):
    print(i)

# 4. Reverse numbers
for i in range(10, 0, -1):
    print(i)

# 5. Print even numbers
for i in range(2, 11, 2):
    print(i)

# 6. Print odd numbers
for i in range(1, 11, 2):
    print(i)

# 7. Loop through a string
name = "Python"

for letter in name:
    print(letter)

# 8. Loop through a list
cities = ["Bengaluru", "Mysuru", "Hubballi"]

for city in cities:
    print(city)

# 9. Nested for loop
for i in range(1, 3):
    for j in range(1, 4):
        print(i, j)

# 10. break statement
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# 11. continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# 12. enumerate()
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]

for index, city in enumerate(cities):
    print(f"City {index}: {city}")

# 13. enumerate() starting from 1
for index, city in enumerate(cities, start=1):
    print(f"City {index}: {city}")

# 14. for-else
for i in range(1, 4):
    print(i)
else:
    print("Completed")

# 15. for-else with break
for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("Completed")

# 16. Sum of numbers from 1 to 10
total = 0

for i in range(1, 11):
    total = total + i

print("Total:", total)

# 17. Sum of even numbers
total = 0

for i in range(2, 11, 2):
    total = total + i

print("Even Total:", total)

# 18. Sum of odd numbers
total = 0

for i in range(1, 11, 2):
    total = total + i

print("Odd Total:", total)

# 19. Multiplication table of 5
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")