"""
One Away: There are three types of edits that can be performed on strings: 
  insert a character, 
  remove a character, 
  or replace a character. 
Given two strings, write a function to check if they are one edit (or zero edits) away. 
"""
# Não entendi pq o primeiro é verdadeiro

def isOneAway(str1, str2):
    count = 0
    for [ltr1, ltr2] in zip(str1, str2): # Orgulhoso dessa linha aqui
        if ltr1 != ltr2:
            count += 1
    
    if count > 1:
        return False

    return True

print(isOneAway("pale", "pie"))        
print(isOneAway("pales", "pale"))        
print(isOneAway("pale", "bale"))        
print(isOneAway("pale", "bake"))        