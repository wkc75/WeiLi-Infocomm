# there is no need to ask for a integer
# the integer should have been given as x, when user uses the function

# version 1: using math
def sum_digit1(x):
    result = 0
    while x != 0:
        # adding result and the last digit of x
        result = result + (x % 10)
        # removing the last digit of x
        x = x // 10

    return result


# version 2: using list
def sum_digit2(x):
    # converting the int x to a string
    x = str(x)
    # creating an empty list
    list_x = []
    # looping throught the string character by character
    for digit in x:
        # for each character in the string
        # convert the character into int
        # then append the int to the list_x
        list_x.append(int(digit))
    
    # return the sum of list_x
    return sum(list_x)

print(sum_digit2(1245))