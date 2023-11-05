# Create a program that ask the user for a number and then prints out a list of all divisors
# of that number.(If you do not know what a divisor is, it is a number that divides evenly into another number.
# for example, 13 is a divisor of 26 because 26\13 has no remainder)

num = int(input("Enter the number:"))
print("Divisor of that number is:")
divisor_list = []
for i in range(1,num+1):
    if (num % i == 0):
        divisor_list.append(i)
print("Divisor list:",divisor_list)
print("The element of divisor list is:",len(divisor_list))
