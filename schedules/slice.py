from planoma.schedules.models import Schedule
from planoma.schedules.course_template import TEMPLATE


# make a queue for a given user id
def makeQueue(pid):
	# for a user id that matches our provided id, get all the course ids in their schedule
	## instead of querying their schedule, we need to query their list of past courses
	pastCourses = (Schedule.objects.filter(owner.id == pid)).course_sessions.courses.objects.values(course_id)

	# create a set from past courses
	# this will be used for set-wise difference to get classes from template still not taken
	p = set(pastCourses)

	## we now have a list of remaining courses
	remainingCourses = [x for x in TEMPLATE if x not in p]

# def slice(remaining_courses, chunk_size):
	