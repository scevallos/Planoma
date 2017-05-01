from schedules.models import *
from constants import *
from django.contrib import messages

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


	# make a new course session for 4848 and fill with remaining courses
	sesh = sched.remaining_courses
	
	for course in remaining_courses:
		sesh.courses.add(Course.objects.get(course_id=course))
		sesh.save()
	sched.course_sessions.add(sesh)
	sched.save()
	# # does forcing a schedule to match our template automatically ensure the correct credit count?????????
	# credit_count = 0
	# for x in past_courses:
	# 	current_course = Course.objects.get(course_id = x)
	# 	credit_count = credit_count + float(current_course.credit)

	return remaining_courses



def makeSchedule(sid):
	sched = Schedule.objects.get(id = sid)

	start_index = getIndex(sched.start_sem, sched)
	end_index = getIndex(sched.end_sem, sched)
	num_semesters = end_index - start_index + 1

	# Some checks about these choices
	try:
		assert end_index > start_index and num_semesters >= 6 and num_semesters <= 11
	except:
		# TODO: figure out best way to handle this
		# TODO: this check above should only happen for like first years e.g junior just tryna make senior yr
		return -1

	# cred_needed = 32 - int(sched.existing_credits)
	# chunk_size = cred_needed / num_semesters


	course_num = 0
	# Loop through courses in template, adding them to the schedule
	for i in xrange(num_semesters):
		sesh = CourseSession(schedule=sched, semester = TERM_CHOICES[start_index + i][0][:2], term = ('20' + TERM_CHOICES[start_index + i][0][-2:]))
		sesh.save()
		for course in xrange(4):
			c = Course.objects.get(course_id = TEMPLATE[course_num])
			sesh.courses.add(c)
			sesh.save()
			sched.course_sessions.add(sesh)
			sched.save()
			course_num += 1

	# Remove the others for extra credits
	if int(sched.existing_credits) >= 1:		
		sched.course_sessions.all().order_by('-term')[0].courses.remove(Course.objects.get(course_id='OTHER4'))
	elif int(sched.existing_credits) == 2:
		sched.course_sessions.all().order_by('-term')[1].courses.remove(Course.objects.get(course_id='OTHER2'))
	sched.save()

	other1 = Course.objects.get(course_id='OTHER1')
	lang1 = Course.objects.get(course_id='LANG1')
	lang2 = Course.objects.get(course_id='LANG2')
	lang3 = Course.objects.get(course_id='LANG3')

	count = 0

	all_sessions = sched.course_sessions.all().order_by('term')
	if sched.languages_completed == '0':
		sesh = all_sessions[3]
		sesh.courses.remove(other1)
		sesh.courses.add(lang1)
		sesh.save()
		sesh = all_sessions[4]
		sesh.courses.remove(other1)
		sesh.courses.add(lang2)
		sesh.save()
		sesh = all_sessions[5]
		sesh.courses.remove(other1)
		sesh.courses.add(lang3)
		sesh.save()
		# for session in sched.course_sessions.all():
		# 	if count = 3:
		# 		break
		# 	else:	
		# 		all_courses = session.courses.all()
		# 		if other1 in all_courses:
		# 			session.courses.remove(other1)

		# 			if count == 0:
		# 				toAdd = lang1
		# 			elif count == 1:
		# 				toAdd = lang2
		# 			elif 
		# 			session.courses.add(lang1)
		# 			count += 1
	elif sched.languages_completed == '1':
		sesh = all_sessions[3]
		sesh.courses.remove(other1)
		sesh.courses.add(lang2)
		sesh.save()
		sesh = all_sessions[4]
		sesh.courses.remove(other1)
		sesh.courses.add(lang3)
		sesh.save()

		# for session in sched.course_sessions.all():
		# 	if count = 2:
		# 		break
		# 	else:	
		# 		all_courses = session.courses.all()
		# 		if other1 in all_courses:
		# 			session.courses.remove(other1)
		# 			session.courses.add(lang2)
		# 			count += 1
	elif sched.languages_completed == '2':
		sesh = all_sessions[3]
		sesh.courses.remove(other1)
		sesh.courses.add(lang3)
		sesh.save()
		# for session in sched.course_sessions.all():
		# 	if count = 1:
		# 		break
		# 	else:	
		# 		all_courses = session.courses.all()
		# 		if other1 in all_courses:
		# 			session.courses.remove(other1)
		# 			session.courses.add(lang3)
		# 			count += 1

	math30 = Course.objects.get(course_id='MATH030')
	math31 = Course.objects.get(course_id='MATH031')
	math60 = Course.objects.get(course_id='MATH060')
	all_sessions = sched.course_sessions.all()
	if sched.math_completed == 'MATH030':
		all_sessions[0].courses.remove(math30)
		all_sessions[0].courses.add(math31)
		all_sessions[0].save()
		
		all_sessions[2].courses.remove(math31)
		all_sessions[2].courses.add(math60)
		all_sessions[2].save()

		all_sessions[1].courses.remove(math60)
		all_sessions[1].courses.add(other1)
		all_sessions[1].save()

	elif sched.math_completed == 'MATH031':
		all_sessions[0].courses.remove(math30)
		all_sessions[0].courses.add(math60)
		all_sessions[0].save()
		
		all_sessions[2].courses.remove(math31)
		all_sessions[2].courses.add(other1)
		all_sessions[2].save()
		
		all_sessions[1].courses.remove(math60)
		all_sessions[1].courses.add(other1)
		all_sessions[1].save()
		
	elif sched.math_completed == 'MATH060':
		all_sessions[0].courses.remove(math30)
		all_sessions[0].courses.add(other1)
		all_sessions[0].save()
		
		all_sessions[2].courses.remove(math31)
		all_sessions[2].courses.add(other1)
		all_sessions[2].save()
		
		all_sessions[1].courses.remove(math60)
		all_sessions[1].courses.add(other1)
		all_sessions[1].save()
		




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
		# TODO: this check above should only happen for like first years e.g junior just tryna make senior yr
		return -1

	cred_needed = 32 - int(sched.existing_credits)
	chunk_size = cred_needed / num_semesters

	# other = Course.objects.get(course_id='OTHER1')

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
