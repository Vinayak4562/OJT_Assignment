res = ""
string = input("Enter the string : ")
n = len(string)
i = 0

while i < n:
    char = string[i]

    if char.isdigit():
        res += char
        i += 1
    else:
        j = i+1
        count = 1
        while char == string[j]:
            count += 1
            j += 1
        res += char
        res += str(count)
        i = j

print(res)