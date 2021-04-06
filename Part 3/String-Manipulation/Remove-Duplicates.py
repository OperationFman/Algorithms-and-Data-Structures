string = "Hellooo!!"
result = []

for i in string:
    if i not in result:
        result.append(i)

x = "".join(result)
print(x)