

def reverse_word(sentence):
    i = len(sentence)
    reversed_word = ""
    while i > 0:
        reversed_word += sentence[i - 1]
        i -= 1
    return reversed_word
