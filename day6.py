#list

#creting a list
numbers = [25, 10, 30, 10, 15]
print("Originl list:",numbers)

#assessing items and indexing
print("First item:", numbers[0])
print("last item:", numbers[-1])

#mdifying a list
numbers[1] = 20
print("After modification:", numbers)

#append()
numbers.append(40)
print("After append:", numbers)

#insert()
numbers.insert(1, 5)
print("After insert:", numbers)

#remove()
numbers.remove(30)
print("After remove:", numbers)

#pop()
numbers.pop()
print("After pop:", numbers)

#list length and count
print("length:", len(numbers))
print("count of 10:", numbers.count(10))

#sum and sorting
print("sum:", sum(numbers))
numbers.sort()
print("sorted list:", numbers)

#slicing
print("frist three items:", numbers[:3])

#everse
numbers.reverse()
print("reversed list:", numbers)

#nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Nested list:", matrix)
print("selected item:", matrix[1][1])

#modify nested list
matrix[1][1] = 50
print("updated matrix:", matrix)