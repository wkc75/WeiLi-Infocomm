age_list = [14, 12, 35, 36, 55]

weili_age = age_list[0]
print(weili_age)

print(len(age_list))
for i in age_list:
    print(i)

age_list.append(0)
print(len(age_list))
print(age_list[-1])

age_list.insert(2, 0)

age_list.pop(-1)