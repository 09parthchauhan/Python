#rules for set
'''
1. set do now allow duplicate 
2. set have no indexing/slicing
3. set don't allow mutable data types like list, dict, set
4. set itself is mutable
'''

#create 
s1 = {10 ,20 ,30, 50}
print(s1)

#cannot create an empty set that will be dictionary
s2 = {} # this is a dictionary
print(type(s2))

s = set() #this creates an empty set
print(type(s))

s3 = {1,2,1,2,4,5,4}
print(s3)

new_set ={"hello", 22, 24, True}
print(new_set)