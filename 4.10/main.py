PossibelPalindrome = input("Please Enter A Sentence That You Think Is A Palindrome... ")

PossibelPalindrome = PossibelPalindrome.casefold()

ReversedPossiblePalindrome = reversed(PossibelPalindrome)

if list(PossibelPalindrome) == list(ReversedPossiblePalindrome):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")