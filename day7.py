# Tuples and Sets

# 1. Creating a tuple
fruits = ("apple", "banana", "cherry")
print("Fruits tuple:", fruits)

# 2. Accessing tuple elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 3. Single element tuple
single = ("apple",)
print("Single element tuple:", single)

# 4. Tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print("Combined tuple:", tuple1 + tuple2)

# 5. Tuple methods
numbers_tuple = (1, 2, 3, 1, 1)
print("Count of 1:", numbers_tuple.count(1))
print("Index of 3:", numbers_tuple.index(3))

# 6. Creating a set
numbers_set = {1, 2, 2, 3, 4}
print("Set:", numbers_set)

# 7. Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric difference:", a ^ b)

# 8. Set methods
fruits_set = {"apple", "banana", "cherry"}
fruits_set.add("orange")
print("After add:", fruits_set)

fruits_set.discard("banana")
print("After discard:", fruits_set)
