from schedules.models import *
from constants import *


########################### TODO:
## prepare the data for making a queue
## if a user has selected any of the modfier options, add them to a schedule with their user id
## then this makequeue fetches the schedule with their id and gets all the courses already in it
## Add lang if they aren't in there, removing some of the others
###########################

def makeQueue(sid):
	"""
		Given a schedule id, creates the queue of courses to take based on TEMPLATE
		minus courses already taken (placed in schedule)
	"""

	# Get the schedule with the given scheduleID
	sched = Schedule.objects.get(id = sid)

	# Get all the courses currently on this schedule
	past_courses = sched.get_all_courses()

	# built a list of past course cids
	past_cids = [course.course_id for course in past_courses]	
	
	# create a set from past courses
	# this will be used for set-wise difference to get classes from template still not taken
	p = set(past_cids)


	# Get reqs specified in schedule form
	sched.languages_completed

	sched.math_completed

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

	


	start_index = TERM_CHOICES.index(start_sem)
	end_index = TERM_CHOICES.index(end_sem)
	

	# if a schedule can't be completed with a given chunk size and start/end sem,
	# ERROR
	#if ((end_index - end_index) * chunk_size) < (32 - credit_count) error

	# iterate through the remaining courses and add them to the schedule
	for x in remaining_courses:
		if (x % chunk_size == 0):
			start_index += 1 # if we have met the chunk size, increment the term index

		###### make a query to look up a course with x as the course_id
		to_add = Course.objects.get(course_id = x)		
		# course = Schedule.course_sessions(semester = TERM_CHOICES[start_index][:2], 
		# 								  term = ('20' + TERM_CHOICES[start_index][-2:])).courses(course_id = x, 
		# 								  course_name = to_add.course_name, area = to_add.area,
		# 								  overlay = to_add.overlay, credit = to_add.credit) # Fix: add support for area, course name, and overlay
		course = sched.course_sessions(semester = TERM_CHOICES[start_index][:2], 
										  term = ('20' + TERM_CHOICES[start_index][-2:])).courses(course_id = x, 
										  course_name = to_add.course_name, area = to_add.area,
										  overlay = to_add.overlay, credit = to_add.credit) # Fix: add support for area, course name, and overlay

		course.save()


def makeBlankSchedule(remaining_courses, sid):

	sched = Schedule.objects.get(id = sid)
	start_index = getIndex(sched.start_sem, sched)
	end_index = getIndex(sched.end_sem, sched)

	# Calculate how many semesters this is
	num_semesters = end_index - start_index + 1
	
	# Some checks about these choices
	try:
		assert end_index > start_index and num_semesters >= 6 and num_semesters <= 11
	except:
		# TODO: figure out best way to handle this
		print 'Error: Invalid start and end semester!'
		exit()

	cred_needed = 32 - int(sched.existing_credits)
	chunk_size = cred_needed / num_semesters

	other = Course.objects.get(course_id='OTHER')

	for x in xrange(1, cred_needed + 1):
		if (x % chunk_size == 0):
			sesh = CourseSession(schedule=sched, semester = TERM_CHOICES[start_index][0][:2], term = ('20' + TERM_CHOICES[start_index][0][-2:]))
			sesh.save()
			sched.course_sessions.add(sesh)
			sched.save()
			# for i in xrange(chunk_size):
			# 	sesh.course.add(other)
			# sesh.save()
			start_index += 1 # if we have met the chunk size, increment the term index



		# fill schedule with others
		#other = Course.objects.get(course_id = 'OTHER')
		# course = sched.course_session(semester = TERM_CHOICES[start_index][:2], 
		# 								  term = ('20' + TERM_CHOICES[start_index][-2:])).courses(course_id = 'OTHER', 
		# 								  course_name = 'Other course', area = None,
		# 								  overlay = None, credit = '1.00')
		# course.save()

def getIndex(term_id, schedule):
	for i in xrange(len(TERM_CHOICES)):
		if TERM_CHOICES[i][0] == term_id:
			return i