statement = "My name is Ifra"
words = statement.split(' ')
string = []
for word in words:
    string.insert(0, word)
print(" ".join(string))
