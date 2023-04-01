dict1 = {'name': 'Msys', 'Place': 'Pune'}
dict2 = {'EmpID': 1, 'Salary': 50000}
dict1.update(dict2)                         # mearging the Dictinory dict1 and dict2.
print(f'After Updating mearging: {dict1}')

salary = dict1['Salary']
new_salary = int(salary * 1.1)              # 10% increment in salary
dict1['Salary'] = new_salary                # new salary apedated.
print(f'After 10% incrimenting: {dict1}')

dict1['age'] = 35                           # Age updated here
print(f'After Updating the Age: {dict1}')

keys = ()
values = ()

for key, value in dict1.items():             # this loop will run till all the Keys and Values are itterated
    keys += (key,)                           # upadting key in keys tuple
    values += (value,)                       # upadting value in values tuple

print(f'Keys in Tuple: {keys}')
print(f'Values in Tuple: {values}')

dict1.pop('age')                            # Removing the Age from dictionary 
# print(f'After removing the Age: {dict1}')

# dict1 = {'name': 'Msys', 'Place': 'Pune'}
# dict2 = {'EmpID': 1, 'Salary': 50000}
# dict = {**dict1, **dict2}
# print(dict)