import os
# file_path = 'C:/Users/Admin/PycharmProjects/pythonproject1/Fibonacchi.py'

cwd = os.getcwd()
print(cwd)
# file_path = cwd+'\hi.txt'
file_path = 'C:/Users/Admin/PycharmProjects/pythonproject1/gyan.txt'

with open(file_path,'r') as file:
    contents = file.read()
    # file.close()
print(contents)

# import os
#
# file_path = 'C:/Users/Admin/PycharmProjects/hi.txt'  # Use the correct absolute path
#
# # Check if the file exists
# if os.path.exists(file_path):
#     # Open the file in read mode
#     with open(file_path, 'r') as file:
#         # Read the contents of the file
#         contents = file.read()
#
#     # Print the contents of the file
#     print(contents)
# else:
#     print(f"File not found: {file_path}")
