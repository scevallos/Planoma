import os
import django
import csv

# Setting up encvironemnt
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "planoma.settings")
django.setup()

from schedules.models import Course, PrereqCourses, EquivCourses

parse_none = lambda x: None if x.strip() == 'None' else x

print 'about to load in courses...'
reader = csv.reader(open('courses.csv'), delimiter=',')
for row in reader:
	if row[0] == 'CourseID':
		continue
	else:
		course = Course()
		course.course_id = parse_none(row[0])
		course.course_name = parse_none(row[1])
		course.area = parse_none(row[2])
		course.overlay = parse_none(row[3])
		course.credit = parse_none(row[4])
		course.save()


# print 'about to load in equivalencies...'
# reader = csv.reader(open('equiv_courses.csv'), delimiter=',')
# for row in reader:
# 	if row[0] == 'course_one':
# 		continue
# 	else:
# 		equiv = EquivCourses()
# 		equiv.course_one = Course.objects.get(course_id = row[0])
# 		equiv.course_two = Course.objects.get(course_id = row[1])
# 		equiv.equiv_to = Course.objects.get(course_id = row[2])
# 		equiv.save()

# print 'about to load in preqreqs...'
# reader = csv.reader(open('prereq_courses.csv'), delimiter=',')
# for row in reader:
# 	if row[0] == 'pre_req':
# 		continue
# 	else:
# 		req = PrereqCourses()
# 		req.course_req = Course.objects.get(course_id = row[0])
# 		req.course_take = Course.objects.get(course_id = row[1])
# 		req.save()