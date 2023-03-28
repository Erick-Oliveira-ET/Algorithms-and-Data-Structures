"""
  1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures? 
"""

def isAllUnique(arr):
    mapItems = set()

    for item in arr:
        if item in mapItems:
            return False
        mapItems.add(item)
    return True

print(isAllUnique([1,2,3,4,3]))
print(isAllUnique([1,2,3,4]))
print(isAllUnique("abacc"))
print(isAllUnique("abc"))

def isAllUniqueWithoutDataStructure(arr):
    arr = sorted(arr)
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            return False
    return True

print(isAllUniqueWithoutDataStructure([1,2,3,4,3]))
print(isAllUniqueWithoutDataStructure([1,2,3,4]))
print(isAllUniqueWithoutDataStructure("abacc"))
print(isAllUniqueWithoutDataStructure("abc"))