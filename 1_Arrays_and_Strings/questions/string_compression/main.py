"""
1.6 - String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
 For example, the string aabcccccaaa would become a2blc5a3, If the "compressed" string would not become smaller than the original string,
 your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z). 

"""

def compressString(string):
    count = 1
    letter = string[0]

    res = ""

    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            res += letter + str(count)
            count = 1
            letter = string[i]
    
    # Last aggregate of same letters can't be compared in the loop
    res += letter + str(count)
    
    return res

print(compressString("aabcccccaaa"))