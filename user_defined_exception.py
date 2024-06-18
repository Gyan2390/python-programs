# user-defined exceptions
class InvalidAgeException(Exception):
    pass

num=18

try:
  in_num = int(input("enter a no. : "))
  if in_num < num:
      raise InvalidAgeException
  else:
      print("Eligible to vote")

except InvalidAgeException:
    print("error occurred: Invalid Age")