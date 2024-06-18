

import re

string = '2102 1111, 39801 356'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string)

if match:
  print(match.group())
else:
  print("pattern not found")

print(match.group(1))
print(match.group(2))
print(match.group(1,2))
print(match.groups())

print(match.start())
print(match.end())
print(match.span())

print(match.re)
print(match.string)