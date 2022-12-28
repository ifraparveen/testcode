print('There are 4 choices available:')
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
counter = 1
while counter <= 3:
    choice = int(input("Enter the choice:"))
    if choice in (1,2,3,4):
        num1 = int(input("Enter 1st number:"))
        num2 = int(input("Enter 2nd number:"))
        if choice == 1:
            add = num1 + num2
            print('sum of', num1, 'and', num2, 'is:', add)
            break
        elif choice == 2:
            dif = num1 - num2
            print('difference of', num1, 'and', num2, 'is:', dif)
            break
        elif choice == 3:
            mul = num1 * num2
            print('product of', num1, 'and', num2, 'is:', mul)
            break
        elif choice == 4:
            div = num1 / num2
            print('division of', num1, 'and', num2, 'is:', div)
            break
    else:
        counter += 1
        print("Wrong choice")
        if counter==4:
            print("Retry exhausted")
        else:
            print("Try again")



