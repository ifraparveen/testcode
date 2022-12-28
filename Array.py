# Declare an array with five element of int data types.Now add three element to this array and print the final array

import array as arr
a = arr.array('i', [1,2,3,4,5,9,18,20,21])
size = len(a)
print("The length of array before adding the element:",size)
print("Before adding the element")
for i in range (0, size):
    print (a[i], end = " ")
print("\r")
a.extend([6,7,8])
size = len(a)
print("the length of array after the element:",size)
print("After adding element:")
for i in range(0,size):
    print(a[i], end=" ")
print("\r")

