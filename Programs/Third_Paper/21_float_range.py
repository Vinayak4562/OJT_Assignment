# def float_range(start, stop, step):
#     while start < stop:
#         yield start             # yield will return one by one output
#         start += step           # incrementing the start with a step

# start = float(input("Enter the Start Value: "))
# stop = float(input("Enter the end Value: "))
# step = float(input("Enter the step Value: "))   
# for num in float_range(start, stop, step):          # running the for loop to itterate the num
#         print(num)

        

def float_range(start,end,step):
    for i in range(int((end - start) / step)):
        value = start + i * step       
        print(round(value,2))
    
start = float(input("Enter the Start Value: "))
end = float(input("Enter the end Value: "))
step = float(input("Enter the step Value: "))

float_range(start,end,step)
