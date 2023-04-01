def is_iterator(iterable):
    try:
        iter(iterable)
        return iter(iterable) is iterable
    except TypeError:
        return False

print(is_iterator([1,2,3]))
print(is_iterator(iter([])))

print(is_iterator(("Vinayak")))
print(is_iterator(iter("Vinayak")))

print(is_iterator({1:20,2:30,3:40}))
print(is_iterator(iter({1:20,2:30,3:40})))

print(is_iterator((1,2,3,4)))
print(is_iterator(iter((1,2,3,4))))
 

