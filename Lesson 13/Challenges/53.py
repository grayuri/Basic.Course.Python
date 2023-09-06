word = input("Type a word (or a phrase): ")
word = word.strip()
wordLength = len(word)

isPalindrome = False

for i in range(0, wordLength):
  if (word[ i : (i+1) ] == word[ wordLength-i-1 : (wordLength-i-1) + 1]):
    isPalindrome = True
  else:
    isPalindrome = False

if(isPalindrome): 
  print("'{}' is a palindrome".format(word))
else: 
  print("'{}' isn't a palindrome".format(word))