
import re

string = "python is fun"

match = re.search('\Apython', string)

if match:
    print("pattern found inside the string")
else:
    print("pattern not found")