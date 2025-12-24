letters = [
    'A','b','C','D','E','F','G','H','i','_','k','l','n','M','N','O','P','Q','R','S','T','U','v','w','x','y','z'
]

v = input("Enter letter:")

for i in range(len(letters)):
    if letters[i] == '_':
        letters[i] = v

print(letters)
