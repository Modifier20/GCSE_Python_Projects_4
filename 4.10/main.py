
SENTENCE = str(input("Please enter a sentence here... "))

word_list = SENTENCE.split()
reversed_list = word_list[:: -1]
PALINDROME = " ".join(reversed_list)

if SENTENCE == PALINDROME:
    print("Your Sentence is a Palidrome...")
elif SENTENCE != PALINDROME:
    print("Your Sentence is not a Palidrome...")
else:
    print("You Haven't Entered A Sentence!")