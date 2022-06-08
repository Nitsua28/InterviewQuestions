'''
Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phase that is the same
 forwards and backwards. A permutation is a rearrangement of letters.
 The palindrome does not need to be limited to just dictionary words.
'''

def palindrome(str):
    hash = {}
    noSpaceCount = 0
    for i in str:
        if i != " ":
            temp = i.lower()
            noSpaceCount += 1
            if temp not in hash:
                hash[temp] = 1
            else:
                if hash[temp] == 1:
                    hash[temp] = 0
                else:
                    hash[temp] = 1
    count = 0
    for j in hash.values():
        if j == 1:
            count += 1
    if noSpaceCount % 2 == 0 and count == 0:
        return True
    elif noSpaceCount % 2 == 1 and count == 1:
        return True
    else:
        return False
#O(n) runtime
#O(n) space


'''
Constraints
0<len(str) < 999
case sensitive and weird characters and spaces

regular cases - tests captial letters, spaces, odd/ even
'''

print("is palin odd")
print(palindrome("Tact Coa"))

print("is palin even")
print(palindrome("U u olloee"))

print("is not palin odd")
print(palindrome("  ehehiuo"))

print("is not palin even")
print(palindrome("  ttkejjne"))

'''
extreme - 0-1 str length
'''

print("empty string")
print(palindrome(""))

print("one len")
print(palindrome("a"))

print("2 len")
print(palindrome("an"))
