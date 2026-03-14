#create 
careers = ("backend engineer", "frontend engineer", "network engineer")
print(careers)

names = ("parth")
print(type(names))

#you can never make a tuple with single element, always adda comma at the end for single item tuple
names = ("parth",)
print(names)

#creating tuple from list
lists = tuple(["parth", "khushal", "yash"])
print(lists)
print(type(lists))

#accessing items
print(careers[-1])
print(careers[0:-1])

#the main difference between list and tuple is editing, list can be edited that is mutable but tuple cannotot be so it is immutable
#careers[0] = "fullstack engineer" #this gives error 
#you can also not add or append items to a tuple

del lists
#del careers[0] #this gives error as you cannot delete an single item

#for i in careers:
#    print(i)

numbers = [10, 1, 43, 2, 764, 2345, 20]
print(sorted(numbers, reverse=True))

#tuples are read-only data type
