word = input("Enter the word:")

lists = list(word)

reverse = lists[::-1]
reverse_word="".join(str(i) for i in reverse)


if lists == reverse:
    print(f"{word} is a palindromic word its reverse is {reverse_word}")
else:
    print(f"{word} is not a palindromic word its reverse is {reverse_word}")    


