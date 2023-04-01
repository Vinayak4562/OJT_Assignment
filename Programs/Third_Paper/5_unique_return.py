def uniques_only(iterable):                   # Returns a new iterable with duplicates removed    
    present = set(iterable) 
    print(present)                            # creating a set of the items that have been Present
    # unique_items = []                       # Took empty list to store the unique items
    # for item in iterable:                   # this loop will run till last item frim iterable
    #     if item not in present:             # if item is not in the Present list it will do append and add.
    #         unique_items.append(item)       # append the item in to the unique_items list
    #         present.add(item)               # it will add to the element in to Present set
    # return unique_items                     # returning the unique_items


original = [1, 2, 2, 1, 1, 3, 2, 1]
uniques = uniques_only(original)
print(uniques)                          #Out Put:[1, 2, 3]

