'''
Implement an algorithm to determine if a string has all
 unique characters.  What if you cannot use additional data structures?
'''
def isUnique(exStr):

    ordered = sorted(exStr) #sorts a string, two pointer method
    for i in range(len(ordered) - 1):
        if ordered[i] == ordered[i+1]:
            return False
    return True

#O(nlogn) runtime because of sorted
#O(n) space? depending on sort


'''
Constraints
0<len(exstr)<999
a<element< z

test cases
'''

'''
regular unique
'''
print("regular unique")
print(isUnique("abc"))

'''
regular not unique
'''
print("regular not unique")
print(isUnique("bbc"))

'''
extreme
'''

print("extreme 2 len unique")
print(isUnique("ab"))

print("extreme 2 len ununique")
print(isUnique("bb"))
