
string1 = "abcbaefabcabchijkl"
given_word = "abc"
n = len(given_word)                 # length of given word is 3
count = 0                           # this count variable is used to count the combinations
list = []
for i in range(len(string1)-n+1):   # length of string is 18 then this loop will run (18 -(3+1))=14 times
    window = string1[i:i+n]
   
    if sorted(window) == sorted(given_word): # it will compair the sorted window with a given word 
        list.append(window)                  # if its equal it will append it to the list
        count += 1                           # it will incriment the count value.

print(f'Total number of combinations are: {count}')
print(f'Combintions are: {list}')

# string2 = "abcbaefabcabchijkl"
# given_word = "abc"
# n = len(given_word)
# count = 0
# list1 = []
# for i in range(len(string2)-n+1):
    