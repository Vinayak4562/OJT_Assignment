def list_to_dict(lst):
    result = {}
    for num in lst:
        str_num = str(num)
        n = len(str_num)//2
        key = int(str_num[:n])
        value = int(str_num[n:])
        result[key] = value
    return result

list1 = [2323, 82, 129388, 95]
dict1 = list_to_dict(list1)
print(dict1)