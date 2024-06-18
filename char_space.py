
# character count with space
char = "hello world"

# character count without space
# chr = "helloworld"
char_array = list(char)
count = 0
# char_array = [char for char in input_str]
for char in char_array:
  if char != ' ': # for not counting space in the expression
    count=count+1
    print(char)

print(count)
# char_count = len(char_array) #using len keyword for counting the space of the character
# print("the char count is:", char_count)
# print("the char count is:", char_array)
