
word = input("Digite uma palavra: ")

if word == word[::-1]:
    print(word[::-1])
    print("A palavra %s é uma palíndrome"%word)
else:
    print("A palavra %s não é uma palíndrome" % word)