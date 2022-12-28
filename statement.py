# Make a list of string statement with the help of split function

statement  = "My name is Ifra i live in Siyana i study in bca"
world_list = list(statement.split(" "))
print(world_list)
print("The number of word in world_list is:",len(world_list))
if 'Siyana' in world_list:
    print("element exist")
else:
    print("Does't exit")
index = world_list.index('Siyana')
print( "The position of siyana is:",index)


    # split function use with commas use

# thought = "Faliure,is,the,first,step,of,success"
# world_list = list(thought.split(","))
# print(world_list)