#prime no. - 2,3,5,7,11

s = int(input("number: "))

if s == 1:
    print("not a prime no.")

elif s>1:
    for i in range(2, s):
       if (s%i)==0:
           print(s,"is not a prime no.")
           break
    else:
        print(s,"is a prime no.")

else:
    print(s,"is a prime no.")
