
# f = lambda a : a*a
# result = f(7)
# print(result)


# f = lambda a,b : a+b
# result = f(4,6)
# print(result)



from functools import reduce

nums = [3,4,5,7,6,9,12,2]
evens = list(filter(lambda n : n%2==0,nums))
print(evens)

doubles = list(map(lambda n : n*2,evens))
print(doubles)

sum = reduce(lambda a,b : a+b, doubles)
print(sum)