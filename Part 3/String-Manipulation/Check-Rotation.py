# Check if string is one rotation to thr right
def rotation(string, reference):
    string = list(string)
    ref = list(reference)

    string.insert(0, string.pop(-1))

    if string == ref:
        return True
    else: return False

print(rotation('ABCD', 'DABC'))