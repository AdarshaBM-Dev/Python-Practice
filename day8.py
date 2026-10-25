
#Dictionary

student = {
    "name": "Ravi",
    "age": 23,
    "marks": {
        "Python": 90,
        "Math": 85
    }
}

# Access values
print(student["name"])
print(student["age"])
print(student["marks"]["Python"])

# Add a new key
student["city"] = "Hubballi"
print(student)

# Update a value
student["age"] = 24
print(student)

# Dictionary methods
print(student.keys())
print(student.values())
print(student.items())

# get() method
print(student.get("city", "Not Found"))

# update() method
student.update({"language": "Kannada"})
print(student)

# pop() method
city = student.pop("city")
print(city)
print(student)
