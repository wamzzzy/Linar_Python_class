#10 methods for string

name = "Moshood is a boy"
print(name.casefold())#casefold(): used to get version of string suitable for caseless comparison

animal = "dog cat mouse dog"
print(animal.count("dog"))#count(): used to get the number of times a value occur in a string

name2 = "ade is good"
print(name2.encode())#encode(): used to encode the string using the codec registered for encoding.

name3 = "ali"
print(name3.endswith("i"))#endswith(): it returns True if the variable ends with the suffix and False if it doesn't.

name4 = "tunde"
print(name4.startswith("t"))#startswith(): it returns True if the variable starts with the suffix and False if it doesn't.

animal2 = "elephant is big"
print(animal2.istitle())#istitle(): it returns True if the string is a title-cased and False, if it is not.

age = "15"
print(age.isnumeric())#isnumeric(): it returns true if the string is numeric and false, if it is not.

animal3 = "tortoise"
print(animal.isalpha())#isalpha(): Return True if the string is an alphabetic string, False otherwise.

animal4 = "3tiger"
print(animal4.isalnum())#isalpha(): Return True if the string is an alpha-numeric string, False otherwise.

print(age.isdecimal())#isdecimal(): Return True if the string is a decimal string, False otherwise.

#3 methods for integer

age2 = 18
print(age2.is_integer())#is_integer(): Returns True. Exists for duck type compatibility with float.is_integer.
print(age2.bit_length())#Number of bits necessary to represent self in binary.
print(age2.bit_count())#Number of ones in the binary representation of the absolute value of self. Also known as the population count.

#3 methods for float
height = 6.5
print(height.hex())#Return a hexadecimal representation of a floating-point number.
print(height.is_integer())#Return True if the float is an integer.
print(height.conjugate())#Return self, the complex conjugate of any float.