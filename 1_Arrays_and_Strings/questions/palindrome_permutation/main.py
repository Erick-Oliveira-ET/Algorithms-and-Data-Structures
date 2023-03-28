"""
 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
 A palindrome is a word or phrase that is the same forwards and backwards.
 A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
"""

def isPermutedPalindrome(s):
    """
        For it to be a palindrome:
            - It must have a even number of each letter 
            - Just one letter can be Odd (when the size of the string is odd)
    """
    mapLetters = {}

    s = s.replace(" ", "").lower()

    for letter in s:
        if letter in mapLetters:
            mapLetters[letter] += 1
        else:
            mapLetters[letter] = 1
    
    hasOdd = False

    for value in mapLetters.values():
        if value % 2 == 1:
            if hasOdd:
                return False
            else:
                hasOdd = True
    
    return True

print(isPermutedPalindrome("Tact Coa")) # Palindrome: taco cat
print(isPermutedPalindrome("Tat Coa"))