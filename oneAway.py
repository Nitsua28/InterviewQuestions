'''
There are three types of edits that can be performed
on strings: insert a character, remove a character, or replace a character.
Given two strings, write a fucntion to check if they are one edit
away (or zero edits)
'''

def oneAway(str1,str2):
    if str1 == str2:
        return True
    hash = {}
    for i in str1:
        temp = i.lower()
        if temp in hash:
            hash[temp] += 1
        else:
            hash[temp] = 1
    for j in str2:
        temp = j.lower()
        if temp in hash:
            hash[temp] -= 1
        else:
            hash[temp] = 1
    count = 0
    for val in hash.values():
        if val == 1 or val == -1:#insertion or deletion or replacement
            count += 1
    if count == 1 or count == 2:
        return True
    else:
        return False
'''
oneaway("pale","palle")
hash{p:0,a:0,l:-1,e:0}
str1= "pale"
str2= "palle"
i=
j=

val=
count=1
'''
'''
Constraints
0<len(str)< 999
all special characters, characters and whitespace
test cases

regular

'''
print("general true cases")

print(oneAway("pale","pae"))#deletion
print(oneAway("pale","palle"))#insertion
print(oneAway("pale","pabe"))#replacement

print(oneAway("pae","pale"))#other way
print(oneAway("palle","pale"))
print(oneAway("pabe","pale"))
#general false cases
print("general false cases")
print(oneAway("palllle","pae"))
print(oneAway("pae","palllle"))
print(oneAway("pale","bae"))
print(oneAway("bae","pale"))

'''
extreme

'''
print("empty string and same cases")
print(oneAway("",""))
print(oneAway("pale","pale"))
print(oneAway("","bae"))
print(oneAway("bae",""))

print("one char edits")
print(oneAway("b",""))
print(oneAway("b","c"))
print(oneAway("","b"))

print("whitespace")
print(oneAway("pale lendrome","palelendrome"))
print(oneAway("bbb a","bbb  a"))
print(oneAway("   ","        "))
