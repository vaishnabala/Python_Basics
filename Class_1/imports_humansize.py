from humansize import approximate_size

print(approximate_size(4000, a_kilobyte_is_1024_bytes=False))

print(approximate_size(size=4000, a_kilobyte_is_1024_bytes=False))

print(approximate_size(a_kilobyte_is_1024_bytes=False, size=4000)) # works - orderchanged and named

#print(approximate_size(a_kilobyte_is_1024_bytes=False, 4000)) # will not work orderchanged and not named

#print(approximate_size(size=4000, False)) # will not work orderchanged and not named


# Key Highlights
# argment usage - fipped working case, flipped not working case