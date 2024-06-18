# arbitrary function
 #sum of multiple numbers
def f_sum(*nums):
    result = 0

    for num in nums:
        result = result + num

    print("sum= ",result)
#fn call 5 args
f_sum(1,2,3,4,5)
#fn call 2 args
f_sum(4,9)