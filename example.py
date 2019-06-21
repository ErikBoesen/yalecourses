import yalecourses
import os

# "api" name can be whatever is most convenient for your program
api = yalecourses.YaleCourses(os.environ['YALE_API_KEY'])

print(api.courses('CPSC'))
for course in api.courses():
    print(f"{course.id}: {course.name}, {course.description}")
