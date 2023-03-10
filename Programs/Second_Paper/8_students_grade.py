marks = int(input("Enter your marks: "))                                    #Taking User input

if marks < 0 or marks > 100:                                                # checking wether user has sent valid input or not
    print("Invalid marks entered. Please enter marks between 0 and 100.")   # if its greater than 100 it will print the message
else:                                                                       # otherwise it will check for Grades
    if marks >= 91:                                                         # range in between (100–91) printing grade – A1
        grade = "A1"
    elif marks >= 81:                                                       # range in between (90-81) printing grade – A2
        grade = "A2"
    elif marks >= 71:                                                       # range in between (80-71) printing grade – B1
        grade = "B1"
    elif marks >= 61:                                                       # range in between (70-61)printing grade – B2
        grade = "B2"
    elif marks >= 51:                                                       # range in between (60-51) printing grade – C1
        grade = "C1"
    elif marks >= 40:                                                       # range in between (50-40) printing grade – C2
        grade = "C2"
    else:
        grade = "Fail"                                                      # less than 40 it will print "Fail"
        
    print("Your grade is:", grade)
