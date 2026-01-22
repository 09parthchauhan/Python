#import my_module as mm
# from my_module import find_index, test
# import sys
import random 

courses = ['AL', 'ML', 'TOC', 'CN', "WEB"]


x = 1
while x<=20:
    random_courses = random.choice(courses)
    print(f"{random_courses}:{x}")
    x += 1
    if x==10:
        #(f"{random_courses} {x}")
        print(f"Breaking point...")
        break

# index = find_index(courses, 'WEB')
# print(index)
# print(test)

# print(sys.path)
