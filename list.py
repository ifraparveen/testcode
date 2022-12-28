# Declare the list of five elements with string data types.Now add three element and print the final list

name = ["Ram","shyam","ifra","Sam","Seema"]
print("Before adding the element")
print(name)
size_before = len(name)
print("The length before adding the element is:",size_before)
name.extend(["Seeta","Mohan","Raj"])
print("After adding the element")
print(name)
size_after = len(name)
print("The length after adding the element is:",size_after)