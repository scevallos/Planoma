import os
import django
from time import sleep
from datetime import datetime
from pytz import timezone

# Make CSV from online
codes_range = (1047, 2386) # exclusive on the ladder 


import csv

# Setting uo encvironemnt
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pocket.settings")
django.setup()

from schedule.models import Course, CourseSession

course = Course()



# def refresh(student):

for i in ['M', 'F', 'C']:
	print "getting %s"%(i)
	d.get_csv(i)
	# wait until the file has download
	while 'csv' not in os.listdir('.'):
		continue
	sleep(5)

	csv_file = [f for f in os.listdir('csv') if f.endswith('.csv')][0]
	dataReader = csv.reader(open(os.path.join('csv',csv_file)), delimiter=',', quotechar='"')
	for row in dataReader: # TODO: Not inputting all entries from the csv
		print row
		if row[0] == 'Date':
			continue
		hist = History()
		hist.sid = student
		hist.typ = i
		hist.date = timezone('US/Pacific').localize(datetime.strptime(row[0], '%m/%d/%Y %I:%M%p'))
		hist.desc = row[1]
		hist.charge = row[2]
		hist.balance = row[3]
		hist.save()

student.last_update = timezone('US/Pacific').localize(datetime.now())
student.save()
print "Done!"
d.finish()

