# Given a list find the duplicate element if exist and then remove them. And find the total element after removing duplicate

number_list = 1,2,3,4,9,15,2,4,15,17
print("element in the number list is:")
print(number_list)
print("The element in the number list in:",len(number_list))
print("Element are removing the duplicate value is:")
number_set = set(number_list)
print(number_set)
print("Size after removing the duplicate element is:",len(number_set))

    # how many duplicate element in the list
print("Duplicate element in the list is:",len(number_list)-len(number_set))







# power of the number

number = 1,2,3,4,5,6,7
power = [' ']* len(number)
for i in range (len(number)):
    power[i] = number[i] ** 2
print(power)