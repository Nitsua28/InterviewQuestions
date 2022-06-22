'''
Given two strings, write a method to decide if
one is a permutation of the otherwise
'''

def checkPermutation(str1,str2):
    if len(str1) == len(str2): #if strings are not equal length then auto false
        hash = {}
        for i in str1:
            if i in hash:
                hash[i]+= 1
            else:
                hash[i]=1 #for every char in str1 hash it or increment key avaliable
        for j in str2:
            if j in hash: #then eliminate them from hash   
                if hash[j] > 1:
                    hash[j]-=1
                else:
                    hash.pop(i)
        if len(hash) == 0:
            return True
    return False

    #runtime : O(n) where n is the length of the strings
    #space : O(n)
    '''
    brute force

    sortedFirst = sorted(str1)
    sortedSecond = sorted(str2)
    if sortedFirst == sortedSecond: # check for equality ==
        return true
    return False

    #n log n runtime
    #O (n) space
    '''
'''
Constraints
0<len(str1)<999
0<len(str2)<999
a<element<z

test cases

regular
'''
print("Is per")
print(checkPermutation("abcd","dbca"))

print("Isn't per")
print(checkPermutation("abcd","asdf"))

'''
extreme

'''
print("test empty string")
print(checkPermutation("",""))

print("test str1 empty")
print(checkPermutation("","asdf"))

print("test str2 empty")
print(checkPermutation("asdf",""))

print("test one char per")
print(checkPermutation("f","f"))

print("test one char not per")
print(checkPermutation("t","f"))

'''
different lengths
'''

print("str1 longer")
print(checkPermutation("qwertyu","sdkf"))

print("str2 longer")
print(checkPermutation("sdkf","qwertyu"))
