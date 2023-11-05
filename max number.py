 # find the maximum element in the list with the help of max function

number_list = 19,67,90,5,27,98
print("the largest element in the list is:",max(number_list))
print("\r")

# find the largest number in the list without the help of max function

number_list = 19,67,90,5,27,98
print("element in the list is:")
print(number_list)
max = number_list[0]
for num in number_list:
    if (num > max):
     max = num
print("largest element:",max)
