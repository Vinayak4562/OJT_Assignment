def iterator(iterable):
    if iter(iterable) == iterable:
        return True
   
print(iterator([1,2,3]))
print(iterator(iter([])))

print(iterator(("Vinayak")))
print(iterator(iter("Vinayak")))
print(iterator({1:20,2:30,3:40}))
print(iterator(iter({1:20,2:30,3:40})))
print(iterator(iter((1,2,3,4))))
print(iterator(iter((1,2,3,4))))