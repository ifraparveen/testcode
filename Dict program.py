# Creating a dictionary with integer keys:

dict = {1 : 'Ifra', 'Name' : 'Samreen', 3 : 'Ifra'}
print("\n Dictionary with the use of integer keys:")
for x in dict.items():
    print(x)
print("\r")

    # simple print items:

print("Items of the Dictionary:")
for x,y in dict.items():
    print(x,y)


# print all the values of dictionary with the help of for loop:

print("values of the dictionary:")
for x in dict:
    print(dict[x])


    # with the help of values.method

# print("values of a dictionary:")
# for x in dict.values():
#     print(x)

# print all the keys of dictionary

# print("Keys of the dictionary:")
# print(dict.keys())

# print keys with the help of for loop

# print("keys of the dictionary")
# for x in dict:
#     print(x)

# creating a dictionary with mixed keys:

# dict = {'Name': 'Ifra', 1: [1,2,3,4]}
# print("\nDictionary with the use of mixed keys:")
# print(dict)

# creating an empty dictinary

# dict = {}
# print("Empty Dictionary")
# print(dict)

# creating a dictionary with dict() method

# Dict = dict({1: 'Ifra', 2: 'samreen', 3: 'Seema'})
# print("\nDictionary with the use of dict():")
# print(Dict)

# creating a dictionary with each item as a pair:

# Dict = dict([(1, 'geeks'),(2, 'for')])
# print("\nDictionary with each item as a pair:")
# print(Dict)

# Adding element one at a time:

# Dict = {}
# print(" Empty Dictionary ")
# print(Dict)
# Dict[0] = 'Ifra'
# Dict[1] = 'Muskan'
# Dict[2] = 4
# print("\nDictionary after adding 3 element:")
# print(Dict)

# Adding set of values to a single keys

# Dict['Value_set'] = 1,2,3
# print("\nDictionary after adding 3 element: ")
# print(Dict)

# updating existing key value:

# Dict[0] = 45
# print("\nupdated key value:")
# print(Dict)

# Adding nested key value to dictionary:

# Dict[5] = {'Nested': {'1': 'Life', '2': 'Money'}}
# print("\nAdding a nested key:")
# print(Dict)

# Aceess the element:

# print("Accessing the element using the key:")
# print(Dict[1])
# print(Dict['Value_set'])

# acessing a element using get() method

# print("Accessing the element using get:")
# print(Dict.get(4))
# print(Dict.get(5))