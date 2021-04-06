def reverseWords(string):
    array = string.split()
    reverse = " ".join(array[::-1])
    return(reverse)

string = "A surprise to be sure but a welcome one"

print(reverseWords(string))