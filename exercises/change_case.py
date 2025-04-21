# .islower() checks if the character is in lower case
# if char is in lower case, it returns true, otherwise it returns false
# same for .isupper()

def  change_case(s):
    # creating a empty string
    result = ""
    # looping through the string, one character after one
    for char in s:
        # checking if the character is in lower case
        if char.islower():
            # if it is in lower case
            # change the character to upper case and append it to the end of result
            result += char.upper()
            # checking if the character is in upper case
        elif char.isupper():
            # if it is in upper case
            # change the character to lower and append it to the end of result
            result += char.lower()
        else:
            # if the character is neither upper or lower 
            # it is not a alphabet
            # thus there is no need to change case
            result += char
    return result

print(change_case("AbCdEfG"))