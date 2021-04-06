def anagrams(string1, string2):
    string1 = list(string1)
    string2 = list(string2)
    
    for i in string1:
        if i in string2:
            string2.pop(string2.index(i))
        else:
            return False
    return True


print(anagrams('abcd', 'badc'))