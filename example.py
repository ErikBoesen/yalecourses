import yalecourses
import os

# "api" name can be whatever is most convenient for your program
api = yalecourses.YaleCourses(os.environ['YALE_API_KEY'])

courses = api.courses('CPSC')
print('There are %d courses in this subject area' % len(courses))
for course in courses:
    print(f"{course.number}: {course.name}, {course.classpath}")
