# dict = {"name":"Akshay", "age":"26", "address":"Bangalore", "pin":"560058", "state":"Karantaka"}
# list1 =[]
# list2 = []

# list1= list(dict.keys())
# print(list1)

# list2 = list(dict.values())
# print(list2)

# list1.sort()
# print(list1)

# list2.sort()
# print(list2)

import new1

class Test2:
    def func3(self):
        print("This is from new file..")


new1.Monkey.func1 = Test2.func3 # filename.classname.functionname = class.function
b = new1.Monkey()
b.func1()

