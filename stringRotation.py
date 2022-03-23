'''
Assume you have a method isSubstring which
checks if one word is a substring of another.
 Given two strings, s1 and s2, write code to check if s2
 is a rotation of s1 using only one call to isSubstring.
'''
def stringRotation(exStr1,exStr2):
    if len(exStr1) == len(exStr2) and len(exStr1) > 0:
        newStr = exStr1 + exStr1
        return True if exStr2 in newStr else False

print(stringRotation("waterbottle","erbottlewat"))
print(stringRotation("waterbottle","alskfmla"))
