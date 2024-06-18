
from itertools import count

infinite_iterator = count(5)

for i in range(5):
    print(next(infinite_iterator))