'''
Write a method to replace all spaces in a string with '%20'. You may assume
that the string has sufficient space at the end to hold the additional
characters, and that you are given the "true" length of the string.
'''
def urlify(str):
    tempStr= ""
    for i in str:
        if i == " ":
            tempStr += "%20"
        else:
            tempStr += i
    return tempStr
#O(n) runtime
#O(n) space?

'''
Constraints
0<len(str)<999
any char

test cases
regular
'''
print("test spaces and not spaces function")
print(urlify(" aus ti n    "))

'''
extreme
'''
print(urlify(""))
print(urlify(" "))
print(urlify("a"))
