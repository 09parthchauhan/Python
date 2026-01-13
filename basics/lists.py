courses = ['AI', 'ML', 'TOC', 'CD']
numbers = [34, 201, 1 ,10 ,45,6,266]

#print(courses)
# print(len(courses))
# print(courses[3])
# print(courses[-1])

# print(courses[:2])

#add item to list
courses.append('Backend')
print(courses)

#add item on specific location
courses.insert(1, 'CN')
print(courses)

subjects = ['frontend', 'maths']

courses.extend(subjects)
print(courses)

#remove items
courses.remove('frontend')
print(courses)


popped = [courses.pop()]
print(courses)
print(popped)

courses.reverse()
print(courses)

courses.sort()
print(courses)

#numbers.sort()
#print(numbers)

sorted_numbers = sorted(numbers)
print(numbers)
print(sorted_numbers)

print(courses.index('ML'))

for item in enumerate(courses, start=1):
    print(item)
    