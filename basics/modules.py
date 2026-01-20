#import my_module as mm
from my_module import find_index, test
import sys

courses = ['AL', 'ML', 'TOC', 'CN', "WEB"]

index = find_index(courses, 'WEB')
print(index)
print(test)

print(sys.path)