dict1 = {1:"I", 2:"II",3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", 
        10:"X",40:"IL",50:"L", 90:"IC", 100:"C",400:"ID", 500:"D",900:"IM",1000:"M"}

num = 2345
res = ""
while  num:
    temp = 0
    for i in reversed(dict1.keys()):       
        if num >= i:
            temp = i
            break
    num -= temp
    res += dict1[temp]
print(res)
          