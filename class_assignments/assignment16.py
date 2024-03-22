#dictionary methods

st_info = {'name':'Moshood','school':'Linar','age':20}
print(st_info.clear())
print(st_info.copy())
print(st_info.get('name'))#Return the value for key if key is in the dictionary, else default.
print(st_info.items())
print(st_info.keys())
print(st_info.setdefault('name'))
print(st_info.update())
print(st_info.values())
print(st_info.fromkeys('school'))#Create a new dictionary with keys from iterable and values set to value.
print(st_info.pop('Moshood'))#If the key is not found, return the default if given; otherwise, raise a KeyError.
print(st_info.popitem())