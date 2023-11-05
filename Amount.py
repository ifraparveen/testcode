amount = int(input("Enter the amount"))
if(amount <= 2):
    print("Couple")
elif(amount > 2 and amount < 5):
    print("Few")
elif(amount <= 5):
    print("Several")
else:
    print("Many")
