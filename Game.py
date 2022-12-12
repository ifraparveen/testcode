import random
def generateRandomNum():
    num = random.randint(1,100)
    print(num)
    return num
choice = 'yes'
while(choice=='yes'):
    random_num = generateRandomNum()
    for x in range(0,5):
        n = int(input("Enter the number:"))
        if (n>random_num):
            print("Your number is too high")
        elif(n<random_num):
            print("Your number is too low")
        elif(n==random_num):
            print("Number is correct.You win")
            break
        if(x==4):
            print("Your attempt is over.You loose")
    choice = input("Do you want to play again:")













