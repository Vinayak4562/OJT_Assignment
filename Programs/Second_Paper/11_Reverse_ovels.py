def reverse_vowel(s):
    vowels = set('aeiouAEIOU')
    s = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] in vowels and s[j] in vowels:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        elif s[i] in vowels:
            j -= 1
        else:
            i += 1
    return ''.join(s)


s = 'HelloeeOO'         #Only vowels are reversed Consonants are at same place.
reversed_vowels = reverse_vowel(s)
print(reversed_vowels)  # output: HOllOeeoe


# def reverse_vowel(s):
#     vowels = set('aeiouAEIOU')
#     return ''.join([s[i] if s[i] not in vowels else next((s[j] for j in range(len(s)-1,i-1,-1) if s[j] in vowels), s[i]) for i in range(len(s))])

