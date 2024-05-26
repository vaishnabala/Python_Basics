from a_humansize import approximate_size
'''here from a_humansize file the definition approximate_size is imported and used'''
print(approximate_size(4000, a_kilobyte_is_1024_bytes=False))

print(approximate_size(size=4000, a_kilobyte_is_1024_bytes=False))

print(approximate_size(a_kilobyte_is_1024_bytes=False, size=4000)) # works - orderchanged and named

#print(approximate_size(a_kilobyte_is_1024_bytes=False, 4000)) # will not work orderchanged and not named

#print(approximate_size(size=4000, False)) # will not work orderchanged and not named

print(approximate_size.__doc__)
print(approximate_size.__name__)
''' All are objects in python , here approximate_size is also an object, every variable is an object, 
every class is an object and everything in python is an object''' 

# Learning Key Highlights
# Argment usage - fipped working case, flipped not working case
# When you need a function, just declare it.
# All are objects in python.
# everything in Python is an object. Strings are objects. Lists are objects. Functions are objects. Classes are objects. Class instances are objects. Even modules are objects.