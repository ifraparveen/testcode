# # program to sum all the elements of a list:
#
# num = 5 ,6, 4, 2, 35, 9
# result = sum(num)
# print(result)

# program to append data of the second list to the first list:

# list1  = [32,44,5,6,12]
# list2 = [22,3,5,44,9]
# for i in range(len(list2)):
#     list1.append(list2[i])
# print(list1)

# program to enter or append n numbers in a list:

num = []
n = int(input("How many element you want to enter:"))
count = 1
for i in range(n):
    x = input(f"Enter element at index{count}:")
    count += 1
    num.append(x)
print(num)


# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# l1 = []
# l2 = []
# for i in list1:
#     if len(i)==0:
#         l1.append(i)
#     else:
#         l2.append(i)
# print(l2)