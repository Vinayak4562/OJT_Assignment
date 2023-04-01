# def is_iterator(iterable):
#     try:
#         iter(iterable)
#         return iter(iterable) is iterable
#     except TypeError:
#         return False

# print(is_iterator([1,2,3]))
# print(is_iterator(iter([])))

def is_iterator(iterable):
    if iter(iterable) is iterable:
        return True           
print(is_iterator(iter([]))) # It is an iterator so its returning True
print(is_iterator([1,2,3]))  # It is not an iterator becuse its dosent have an iter method.