intro = "My_name_is_weili_and_I_am_14_years_old"

# len()
# takes in a string
# return the length of the string
length = len(intro)
print(length)

# .upper()
print(intro.upper())

# .lower()
print(intro.lower())

print(intro)

# index
print(intro[4] + intro[5])

# string[start : end]
# it is inclusive of the start 
# it is not inclusive of the end
name_intro = intro[0:16]
print(name_intro)

# indexing from the end
print(intro[-8])

# print in reverse
print(intro[::-1])