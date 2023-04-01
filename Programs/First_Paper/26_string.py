S = input("Enter string S: ")
k = input("Enter string k: ")

start_index = S.find(k)
if start_index == -1:
    print((-1, -1))
else:
    end_index = start_index + len(k) - 1
    print((start_index, end_index))
    while True:
        start_index = S.find(k, start_index + 1)
        if start_index == -1:
            break
        end_index = start_index + len(k) - 1
        print((start_index, end_index))

# OutPut:
# Enter string S: aaahaa
# Enter string k: aa
# (0, 1)
# (1, 2)
# (4, 5)