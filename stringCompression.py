'''
Implement a method to perform basic string compression using the counts of
repeated characters.  For example, the string aabcccccaaa would become a2b1c5a3.
 If the "compressed string" would not become smaller than the original strings
 then return the original. You can assume the string only has uppercase
  and lowercase letters
'''

def stringComp(exStr):#two pointers
    if len(exStr) < 3:
        return exStr
    newStr= ""
    prev = exStr[0]
    count = 0
    for i in exStr:
        if i == prev:
            count += 1
        else:
            newStr+=prev + str(count)
            count = 1
        prev = i
    newStr+=prev + str(count)
    if len(exStr)< len(newStr):
        return exStr
    else:
        return newStr
'''
runtime: O(n)
space: O(n)

Constraints
0<len(n)< 999
only upper and lower char

regular - upper and lowercase, general cases
'''
print("Regular----")

print(stringComp("aabcccccaaa"))

print(stringComp("TTbccctt"))

'''
extreme cases - empty strings and one character
'''

print(stringComp(""))

print(stringComp("a"))

print("lots of sequencal characters")

print(stringComp("aaaaaaaabbbbccccccccccccd"))
