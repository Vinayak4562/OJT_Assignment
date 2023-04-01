# def last_lines(file_path, num_lines=10):
   
#     with open(file_path, 'r') as f:              # Open the file in read mode
        
#         lines = f.read().splitlines()            # Read the entire file and split it into lines
        
#         return lines[-num_lines:][::-1]          # Return the last num_lines lines in reverse order
    
# for line in last_lines('my_file.txt'):
#     print(line)

# for line in last_lines('my_file.txt', 5):
#     print(line)


file = open(r"D:\Msys_Programs\MSys_Projects\PythonProg\Task\my_file.txt", "r")
new = file.readlines()
rev = new[::-1]
for i in rev:
    i = i.replace("\n" , "")
    print(i)
