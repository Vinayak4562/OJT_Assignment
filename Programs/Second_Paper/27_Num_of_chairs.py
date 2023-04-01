simulated = ['CCRLU', 'CRLCUC', 'CCCR']
avlalable_chairs = 0
num_chairs = 0
for i in simulated:
    for j in i:                 
        if j == "C" :                           # C - A new employee comes to work area and new chair need to purchase
            if avlalable_chairs == 0 :          # Checking the avalabality of chairs first
                num_chairs += 1                         # if there is no avalabality incriment the chair number
            else:
                avlalable_chairs += 1           # if chairs are not avalable increment the count of avalable chair
        elif j == "R":                          # R - Employee from work area goes to meeting room and free up the chair
            avlalable_chairs -= 1               # Decrement the chair count to allocate the person
        elif j == "U":                          # U - Employee comes from meeting room and occupy the chair
            avlalable_chairs -= 1               # Decrement the chair count to allocate the person
        elif j == "L":                          # L - Leaves the work area and free up the chair
            avlalable_chairs += 1               # Increment the chair count person Leaves the work
    print(f'Minimum number of new chairs to be purchase: {num_chairs}')
    num_chairs = 0                              # re-initializing to 0
    avlalable_chairs = 0                        # re-initializing to 0
