from schedules.models import Schedule
from schedules.course_template import TEMPLATE
from schedules.schedule_options import *

########################### TODO:
## prepare the data for making a queue
## if a user has selected any of the modfier options, add them to a schedule with their user id
## then this makequeue fetches the schedule with their id and gets all the courses already in it
## Add lang if they aren't in there, removing some of the others
###########################

# make a queue for a given user id
def makeQueue(pid, sid):
	# for a user id that matches our provided id, get all the course ids in their schedule
	## instead of querying their schedule, we need to query their list of past courses
	sched = Schedule.objects.filter(owner = pid).filter(id = sid)[0]

	# Getting all the past_courses in this list of Course objects
	past_courses = []
	for session in sched.course_sessions:
		for course in session.courses.all():
			past_courses.append(course)

	past_cids = []
	for course in past_courses
		past_cids.append(course.course_id)
	# built a list of past course cids
	

	# create a set from past courses
	# this will be used for set-wise difference to get classes from template still not taken
	p = set(past_cids)

	## we now have a list of remaining courses
	# this enforces that all areas must be completed
	remaining_courses = [x for x in TEMPLATE if x not in p]

	###############
	##
	## Might be able to avoid this by just adding these when making past courses to begin with, but then we'd also have to remove a few of the others
	##
	if 'LANG1' not in past_courses:
		# replace the first other with lang1
		first_other = remaining_courses.index("OTHER")
		remaining_courses[first_other] = 'LANG1'
		

	if 'LANG2' not in past_courses:
		# replace the next other with lang2
		first_other = remaining_courses.index("OTHER")
		remaining_courses[first_other] = 'LANG2'

	if 'LANG3' not in past_courses:
		# replace the next other with lang3
		first_other = remaining_courses.index("OTHER")
		remaining_courses[first_other] = 'LANG3'

	# # does forcing a schedule to match our template automatically ensure the correct credit count?????????
	# credit_count = 0
	# for x in past_courses:
	# 	current_course = Course.objects.get(course_id = x)
	# 	credit_count = credit_count + float(current_course.credit)

	return remaining_courses



def makeSchedule(start_sem, end_sem, remaining_courses, chunk_size, sid):

	term_index = TERM_CHOICES.index(start_sem)
	end_index = TERM_CHOICES.index(end_sem)
	sched = Schedule.objects.filter(id = sid)[0]

	# if a schedule can't be completed with a given chunk size and start/end sem,
	# ERROR
	#if ((end_index - end_index) * chunk_size) < (32 - credit_count) error

	# iterate through the remaining courses and add them to the schedule
	for x in remaining_courses:
		if (x % chunk_size == 0) term_index++ # if we have met the chunk size, increment the term index

		###### make a query to look up a course with x as the course_id
		to_add = Course.objects.get(course_id = x)		
		# course = Schedule.course_sessions(semester = TERM_CHOICES[term_index][:2], 
		# 								  term = ('20' + TERM_CHOICES[term_index][-2:])).courses(course_id = x, 
		# 								  course_name = to_add.course_name, area = to_add.area,
		# 								  overlay = to_add.overlay, credit = to_add.credit) # Fix: add support for area, course name, and overlay
		course = sched.course_sessions(semester = TERM_CHOICES[term_index][:2], 
										  term = ('20' + TERM_CHOICES[term_index][-2:])).courses(course_id = x, 
										  course_name = to_add.course_name, area = to_add.area,
										  overlay = to_add.overlay, credit = to_add.credit) # Fix: add support for area, course name, and overlay

		course.save()

