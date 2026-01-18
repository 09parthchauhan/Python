language = "Java"

if language == "Python":
    print("Its True")
elif language == "Java":
    print("Yes it is!")
else: 
    print("nope your wrong") 


usr = 'Admin'
logged_in = False

if not logged_in:
    print("Please login")
    logged_in = True
else:
    print("welcome admin")


a = [1,2,3]
b = [1,2,3]

print(id(a))
print(id(b))
print(a is b)

