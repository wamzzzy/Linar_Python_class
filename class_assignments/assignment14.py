#string indexing and string slicing

place = "linar is an ICT school"
print(place[0:5])
print(place[-11:])
print(place[:15])

#list indexing and list slicing
my_exp = ['Tunde', 18, 'Akesan', 6.5]
print(my_exp[0:2])
print(my_exp[2:])
print(my_exp[-3:-1])
print(my_exp[:4])

#list methods
print(my_exp.extend('Tunde'))#Extend list by appending elements from the iterable.
print(my_exp.insert(18,6.5))#Insert object before index.
print(my_exp.pop())#Remove and return item at index (default last). Raises IndexError if list is empty or index is out of range.
print(my_exp.remove('Akesan'))#Remove first occurrence of value. Raises ValueError if the value is not present.
print(my_exp.reverse())
print(my_exp.append('Boy'))#Append object to the end of the list.
print(my_exp.clear())
print(my_exp.copy())#Return a shallow copy of the list.
print(my_exp.count(18))#Return number of occurrences of value.
print(my_exp.sort())#Sort the list in ascending order and return None.
print(my_exp.index('Tunde'))#Return first index of value. Raises ValueError if the value is not present.