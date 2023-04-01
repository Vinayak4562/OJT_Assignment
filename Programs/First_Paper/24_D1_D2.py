import os

source = 'D:\D1'
destination = 'D:\D2'

files = os.listdir(source)
for file in files:
    source_path = os.path.join(source, file)
    destination_path = os.path.join(destination, file)
    os.rename(source_path, destination_path)

print(f'Source path is: {source_path}')
print(f'Destination path is: {destination_path}')