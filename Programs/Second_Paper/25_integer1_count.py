def digit_count(n):
    count = 0                       # Count variable is used to store the digit of count
    for i in range(n+1):            # this for loop will run till n+1 to include last number
        count += str(i).count('1')  #str(i) converts the integer i to its string representation and 
                                    # count('1') counts the number of occurrences of the digit '1' in the string finaly increment the count.
    
    return count                    # Return the count 

n = digit_count(int(input("Enter the number: ")))                       # to take input from user
print(f"Number of digit 1 is occurred {n} times in given range.")       # print the number of occurrence count.‘1’,‘10’,‘11’,‘12’,‘13’