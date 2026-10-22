# Operators

# 1. Arithmetic Operators
print("----- Arithmetic Operators -----")

a = 10
b = 3

print("Addition (+):", a + b)
print("Subtraction (-):", a - b)
print("Multiplication (*):", a * b)
print("Division (/):", a / b)
print("Floor Division (//):", a // b)
print("Modulus (%):", a % b)
print("Exponent (**):", a ** b)


# 2. Assignment Operators
print("\n----- Assignment Operators -----")

x = 10
print("Initial x:", x)

x += 5
print("After += 5:", x)

x -= 3
print("After -= 3:", x)

x *= 2
print("After *= 2:", x)

x /= 4
print("After /= 4:", x)

x = 10
x %= 3
print("After %= 3:", x)


# 3. Comparison Operators
print("\n----- Comparison Operators -----")

a = 10
b = 5

print("Equal (==):", a == b)
print("Not Equal (!=):", a != b)
print("Greater Than (>):", a > b)
print("Less Than (<):", a < b)
print("Greater or Equal (>=):", a >= b)
print("Less or Equal (<=):", a <= b)


# 4. Logical Operators
print("\n----- Logical Operators -----")

a = 15
b = 3

print("AND:", a > 10 and b > 1)
print("OR:", a < 5 or b < 5)
print("NOT:", not a > b)


# 5. Membership Operators
print("\n----- Membership Operators -----")

language = "Python"

print("'P' in language:", "P" in language)
print("'z' in language:", "z" in language)
print("'Java' not in language:", "Java" not in language)


# 6. Bitwise Operators
print("\n----- Bitwise Operators -----")

a = 5
b = 3

print("Bitwise AND (&):", a & b)
print("Bitwise OR (|):", a | b)
print("Bitwise XOR (^):", a ^ b)
print("Bitwise NOT (~):", ~a)
print("Left Shift (<<):", a << 2)
print("Right Shift (>>):", b >> 1)
