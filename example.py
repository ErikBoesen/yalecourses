import yalecourses
import os

# "api" name can be whatever is most convenient for your program
api = yalecourses.YaleCourses(os.environ['YALE_API_KEY'])

courses = api.courses('CPSC')
print('There are %d courses in this subject area:' % len(courses))
for course in courses:
    print(f"- {course.number}: {course.name}")

course = api.course('CPSC201')
print(course.code + ':')
print(course.raw_description)

# If you want more specificity
course = api.course(subject='CPSC', number=201, year=2015, term=1)
print(f'The {course.year} version of {course.code} was taught primarily by {course.instructors[0]}.')
