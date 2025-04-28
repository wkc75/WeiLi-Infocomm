# Pseudo Code
# Function get_even_numbers(numbers):
#     Initialize empty list even_numbers
#     For each number in numbers:
#         If number modulo 2 equals 0:
#             Add number to even_numbers
#     Return even_numbers

def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers