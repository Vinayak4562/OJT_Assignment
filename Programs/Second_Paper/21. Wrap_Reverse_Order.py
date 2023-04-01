def reverse_wrap_string(s, width):
    s = s.replace(" ", "")
    s = s[::-1]
    lines = []
    for i in range(0, len(s), width):
        lines.append(s[i:i+width])
    return "\n".join(lines[::-1])

s = "Hello, welcome to this organisation."
width = 3
result = reverse_wrap_string(s, width)
print(result)