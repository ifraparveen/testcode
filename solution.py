def find_even_odd(nums):
    print("Calling even odd function")
    even = []
    odd = []
    for i in nums:
        if (i % 2==0):
            even.append(i)
        else:
             odd.append(i)
    print("Even List:",even)
    print("Odd List:",odd)



def find_max_number(number_list):
    print("calling largest number")
    max = number_list[0]
    for num in number_list:
        if (num > max):
            max = num
    print("largest element:", max)


def find_smallest_number(nums):
    print("calling smallest number")
    min = nums[0]
    for num in nums:
        if (num < min):
            min = num
    print("Smallest element:", min)




a = [34,87,6,57,22,90]
print("number list are:")
print(a)
#find_even_odd(a)
# find_max_number(a)
#find_smallest_number(a)



def fibonacci_series(x):
    print("fibonacci series of", x, "terms")
    series = []
    t1 =0
    t2 =1
    series.append(t1)
    series.append(t2)
    while (len(series) < x):
        sum = t1+t2
        series.append(sum)
        t1 = t2
        t2 = sum
    print(series)


fibonacci_series(10)



















