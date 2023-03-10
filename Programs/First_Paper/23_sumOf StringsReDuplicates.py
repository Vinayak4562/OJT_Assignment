def highest_sum(s):
    prev_char = ''
    sum = 0
    for c in s:
        if c != prev_char:
            sum += int(c)
            prev_char = c
    return sum

print(highest_sum('1211'))