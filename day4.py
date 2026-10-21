
#  String Manipulation

# 1. String Concatenation (+)
first_name = "Adarsha"
last_name = "BM"

print("Full name: " + first_name + " " + last_name)

# 2. String Repetition (*)
print("Hello! " * 3)

# 3. String Methods
text = "  Hello Python  "

print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("Python", "World"))

# 4. String Indexing
language = "Python"

print(language[0])   # P
print(language[2])   # t
print(language[-1])  # n
print(language[-3])  # h

# 5. String Slicing
print(language[0:3])  # Pyt
print(language[:4])   # Pyth
print(language[2:])   # thon

# 6. Comments
# This is a single-line comment
print("Learning Python")

# 7. Escape Sequences
print("Hello\nPython")
print("Name:\tAdarsha")
print("This is a backslash: \\")

# 8. Greeting Program
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Using concatenation
print("Hello, " + name + "! You are " + str(age) + " years old.")

# Using f-string
print(f"Hello, {name}! You are {age} years old.")

# 9. Character Counter (excluding spaces)
sentence = input("Enter a sentence: ")
character_count = len(sentence.replace(" ", ""))

print(f"Characters excluding spaces: {character_count}")
