
phrase = input("Please enter a string in increasing order: ");

increasing = 0
for letter in range(len(phrase) - 1):
    if ord(phrase[letter]) > ord(phrase[letter + 1]):
        increasing = 1

if increasing == 0:
    print(phrase, "is increasing.")
else:
    print(phrase, "is decreasing.")
