student = {'name' : 'parth',
           'age': 23,
           'courses' : ['AI', 'ML']
           }
print(student['name'])

#print(student.get('age'))
#print(student.get('phone', '"Not found"'))
print(student.items())

student.update({
    'name' : 'yash',
    'age' : 25,
    'courses' : ['Aerospace']
})

print(student)

del student['courses']
print(student)

print(len(student))

for key,values in student.items():
    print(key, values)

