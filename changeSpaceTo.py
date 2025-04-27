def replace_space(string):
    result = ""
    for item in string:
        if item == " ":
            result += "\U0001F600"
        else:
            result += item
    return result

text = "kjsdn     glsnfj vnjd  dfljvn  ld  dfjnvlksfn ndffdv dfj nldfn lkdnklndf lndlfjnkldnldn lfjn dlfn kldfnlfkdn "
print(replace_space(text))