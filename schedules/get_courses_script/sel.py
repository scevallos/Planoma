# -*- coding: utf-8 -*-
# from credentials import USER_ID, PASSWORD
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
from datetime import datetime
import os

from time import sleep
import re

phantomdriver = './phantomjs'
chromedriver = './chromedriver'
url = 'https://aspc.pomona.edu/courses/schedule/'

# driver = webdriver.PhantomJS(executable_path=phantomdriver)
driver = webdriver.Chrome(executable_path=chromedriver)
# elt = driver.find_element_by_link_text('See only these reviews')
# elt = driver.find_element_by_class_name('content')
# elt = driver.find_element_by_id("id_term")
driver.get(url)
driver.find_element_by_xpath("//select[@id='id_term']/option[text()='SP 2017']").click()
driver.find_element_by_xpath("//select[@id='id_department']/option[text()='CSCI - Computer Science']").click()
driver.find_element_by_id('id_c_po').click()
driver.find_element_by_id('submit').click()

sleep(1)
courses = {}
courseList = driver.find_element_by_xpath("//ol[contains(@class, 'course_list')]")
print 'getting courses...'
i = 0
for child in courseList.find_elements_by_xpath(".//*"):

	s = child.text
	s = s.encode('utf-8')
	try:
		# cid = re.findall('[A-Z]+\d+\w+?', s)[0]
		cid = re.findall('(^.*)PO', s)[0].strip()
		cname = re.findall('— (.*)',s)[0].strip()
	except:
		continue
	
	# cname = ' '.join(re.findall('[A-Z][a-z]+',s))
	if cid == '':
		continue
	courses[cid] = cname
	i += 1
	if i % 10 == 0:
		print 'gotten %d courses so far..' % i


for k,v in sorted(courses.iteritems()):
	print k,v
print "There are %d courses offered this semester." % len(courses)
	
# driver.find_element_by_xpath("//div[@id='search_panel']/ol/").click()

exit()


# class DataFetcher:
# 	'''
# 		A Fetcher classes that uses Selenium to login into the cards.cuc website and
# 		can download the CSV files for the last 6 months of the user data
# 	'''

# 	def __init__(self):
# 		self.display = Display(visible=0, size=(800, 600))
# 		self.display.start()

# 		# setting up driver details
# 		chromedriver = "./webdrivers/chromedriver"
# 		chrome_options = webdriver.ChromeOptions()
# 		# specifying download directory for csv files
# 		chrome_options.add_experimental_option("prefs", {"download.default_directory": os.path.join(os.getcwd(), 'csv')})

# 		self.driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
# 		self.skey = ''
# 		self.name = ''
# 		self.userID = USER_ID

# 	def login(self):
# 		'''
# 			Logs into the cuc website, validating skey
# 		'''
# 		self.driver.get('https://cards.cuc.claremont.edu/login.php?cid=35&')
# 		username = self.driver.find_element_by_id("loginphrase")
# 		password = self.driver.find_element_by_id("password")

# 		username.send_keys(USER_ID)
# 		password.send_keys(PASSWORD)

# 		submit_button = self.driver.find_element_by_class_name('submit-form')
# 		submit_button.click()

# 		# Gets skey from URL
# 		self.skey = self.driver.current_url[47:79]

# 		# Wait until page loads, then get name
# 		WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'jsa_account-info')))
# 		self.name = ' '.join(self.driver.find_element_by_class_name('jsa_account-info').get_attribute('innerText').split()[3:5])

# 	def get_csv(self, history_type):
# 		'''
# 			Downloads the 6 month history csv, with validated skey, into 'data' directory;
# 			Gets the claremont cash (C), flex (F), or meal (M) history
# 			:param: type is either 'C', 'F', or 'M' depending on what data is wanted
# 		'''
		
# 		acct = {'M' : 'B20', 'F' : '21', 'C' : '1'}.get(history_type)
# 		if acct:
# 			rn = datetime.today()
# 			csv_url = "https://cards.cuc.claremont.edu/statementdetail.php?cid=35&skey=%s&format=csv&startdate=1887-10-14&enddate=%d-%02d-31&acct=%s" % (self.skey, rn.year, rn.month, acct)
# 		else:
# 			# Invalid history_type
# 			print 'Invalid history_type param passed to get_csv'
# 			exit()
# 		self.driver.get(csv_url)

# 	def finish(self):
# 		'''
# 			Tears down the webdriver and the display
# 		'''
# 		self.driver.close()
# 		self.display.stop()