word = input("Enter a word: ");
vow = 0
con = 0
vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"];
for i in word:
    if (i in vowels):
        vow+=1
    else:
        con+=1
print( word, "has", vow, "vowels and", con, "conconants.")

