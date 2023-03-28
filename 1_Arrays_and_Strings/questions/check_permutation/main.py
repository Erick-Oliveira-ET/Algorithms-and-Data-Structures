"""
  Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
"""

def isPermutation(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    mapArr1 = {}

    for item in arr1:
        if item in mapArr1:
            mapArr1[item] += 1
        else:
            mapArr1[item] = 1
    
    for item in arr2:
        if item in mapArr1:
            mapArr1[item] -= 1

            if mapArr1[item] < 0:
                return False
        else:
            return False
    
    return True

print(isPermutation("aabb", "abab"))
print(isPermutation("aabb", "aba"))
print(isPermutation("aabb", "abac"))
print(isPermutation("aabb", "abaa"))
