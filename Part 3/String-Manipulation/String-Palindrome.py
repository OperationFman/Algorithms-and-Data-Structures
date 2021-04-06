def palindrome(string):
    check = string[::-1]
    if check == string:
        return True
    else: return False

print(palindrome('abcba'))
print(palindrome('abcde'))