# Pseudo Code
# Function count_char(text, char):
#   Initialize counter to 0
#   Convert text to lowercase
#   Convert char to lowercase
#   For each letter in text:
#       If letter equals char:
#           Increment counter
#   Return counter

def count_char(text, char):
    counter = 0
    text = text.lower()
    char = char.lower()
    for letter in text:
        if letter == char:
            counter += 1
    return counter