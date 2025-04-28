# Pseudo Code
# Function reverse_words(sentence):
#     Split sentence into list of words
#     Initialize empty list reversed_words
#     For each word in words:
#         Reverse the characters in word
#         Add reversed word to reversed_words
#     Join reversed_words with spaces
#     Return joined string

def reverse_word(sentence):
    i = len(sentence)
    reversed_word = ""
    while i > 0:
        reversed_word += sentence[i - 1]
        i -= 1
    return reversed_word
