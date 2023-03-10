input = [1, 2, 3, 2, 4, 2, 4, 7, 8, 4, 5, 8, 6, 9, 2]

dict = {}

for i in input:             # to iterate the list
    if i % 2 == 0:          # Used to chek wether num is even or Odd
        if i in dict:       # used to chek wethwer the key is present or not.
            dict[i] += 1    
        else:
            dict[i] = 1

print(dict)  #Out_put:{2: 4, 4: 3, 8: 2, 6: 1}